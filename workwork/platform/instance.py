import logging

import boto3
import botocore.exceptions
from flask import current_app

from workwork.errors import InvalidRegion, InvalidInstanceId, InvalidAction


LOGGER = logging.getLogger(__name__)

def validate_region(region):
    regions = [
        "us-east-1",
        "us-west-2",
        "us-west-1",
        "eu-west-1",
        "eu-central-1",
        "ap-southeast-1",
        "ap-northeast-1",
        "ap-southeast-2",
        "ap-northeast-2",
        "sa-east-1",
    ]

    if region not in regions:
        LOGGER.warn("Invalid region '{}'".format(region))
        print("Invalid region '{}'".format(region))
        raise InvalidRegion


def validate_action(action):
    valid_actions = ["start", "stop", "reboot"]

    if action not in valid_actions:
        LOGGER.warn("Invalid action '{}'".format(action))
        print("Invalid action '{}'".format(action))
        raise InvalidAction


def create_ec2_connection(region, public_key=None, secret_key=None):
    if not public_key:
        public_key = current_app.config["AWS_ACCESS_KEY_ID"]
    if not secret_key:
        secret_key = current_app.config["AWS_SECRET_ACCESS_KEY"]

    return boto3.resource(
        "ec2",
        aws_access_key_id=public_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )


def set_instance_state(instance_id, region, action):
    ec2 = create_ec2_connection(region)

    instances = ec2.instances.filter(InstanceIds=[instance_id])

    try:
        if action == "start":
            instances.start()
        elif action == "stop":
            instances.stop()
        elif action == "reboot":
            instances.reboot()
    except botocore.exceptions.ClientError:
        LOGGER.warn("instance_id not found '{}'".format(instance_id))
        print("instance_id not found '{}'".format(instance_id))
        raise InvalidInstanceId
