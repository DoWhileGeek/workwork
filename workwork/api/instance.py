import logging

import boto3
from flask import Blueprint, current_app
from webargs import fields
from webargs.flaskparser import use_args

from workwork.platform import instance, helpers

blueprint = Blueprint("instance", __name__)
LOGGER = logging.getLogger(__name__)

@blueprint.route("/instance/<instance_id>/<action>/", methods=["GET", "POST"])
@use_args({
    "api_key":  fields.Str(validate=helpers.validate_api_key, required=True),
    "region":   fields.Str(validate=instance.validate_region),
    },
    locations=("json", ),
)
def instance_post(args, instance_id, action):
    instance.validate_action(action)

    instance.set_instance_state(instance_id, action, args.get("region"))

    return "", 204
