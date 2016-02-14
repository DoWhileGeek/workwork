import logging

import boto3
from flask import Blueprint, current_app
from webargs import fields
from webargs.flaskparser import use_args


blueprint = Blueprint("instance", __name__)
LOGGER = logging.getLogger(__name__)

@blueprint.route("/instance/<instance_id>/<action>/", methods=["GET", "POST"])
@use_args({
    "region":  fields.Str(required=False),
    },
    locations=("json",))
def instance_post(args, instance_id, action):
    return "", 204
