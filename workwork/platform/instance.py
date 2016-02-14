import boto3
import botocore.exceptions
from flask import current_app
from webargs import ValidationError

from workwork.errors import InvalidRegion, InvalidInstanceId, InvalidAction


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
        raise InvalidRegion


def validate_action(action):
    valid_actions = ["start", "stop", "reboot"]

    if action not in valid_actions:
        raise InvalidAction


def create_ec2_connection(public_key=None, secret_key=None, region=None):
    if not public_key:
        public_key = current_app.config["AWS_ACCESS_KEY_ID"]
    if not secret_key:
        secret_key = current_app.config["AWS_SECRET_ACCESS_KEY"]
    if not region:
        region = current_app.config["AWS_REGION"]

    return boto3.resource(
        "ec2",
        aws_access_key_id=public_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )


def set_instance_state(instance_id, action, region=None):
    ec2 = create_ec2_connection(region=region)

    instances = ec2.instances.filter(InstanceIds=[instance_id])

    try:
        if action == "start":
            instances.start()
        elif action == "stop":
            instances.stop()
        elif action == "reboot":
            instances.reboot()
    except botocore.exceptions.ClientError:
        raise InvalidInstanceId
