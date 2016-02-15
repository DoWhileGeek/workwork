import logging

import boto3
from flask import Blueprint, current_app
from webargs import fields
from webargs.flaskparser import use_args

from workwork.platform import instance, helpers

blueprint = Blueprint("instance", __name__)
LOGGER = logging.getLogger(__name__)

@blueprint.route("/instance/<region>/<instance_id>/<action>/", methods=["PUT", "POST"])
@use_args({
    "api_key":  fields.Str(validate=helpers.validate_api_key, required=True),
    },
    locations=("json", "headers", "cookies"),
)
def instance_id_update(args, region, instance_id, action):
    instance.validate_region(region)
    instance.validate_action(action)

    instance.set_instance_state(instance_id, region, action)

    return "", 204
