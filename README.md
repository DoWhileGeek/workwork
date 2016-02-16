# workwork [![Build Status](https://travis-ci.org/DoWhileGeek/workwork.svg?branch=master)](https://travis-ci.org/DoWhileGeek/workwork)

A flask api for managing aws ec2 instances.

## Installation:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If there is demand the project could be made pip-able.

## Usage:
This api is built to start, stop, and reboot pre-existing AWS EC2 instances. It is not built to create, or destroy instances. To use the endpoints listed below you must first create an instance on the aws console, or otherwise, and record the region it was created in, and the instance id it was given.

### Set instance state
`POST /instance/<region>/<instance_id>/<action>/`

#### Parameters:
- `api_key`: Api key for this app. Must be supplied as a header, or a cookie, or json.
- `region`: Cannonical AWS region name. e.g. 'us-west-2'
- `instance_id`: AWS supplied instance id. e.g. 'i-abba916a'
- `action`: State to set the instance to. possible options include: ["start", "stop", "reboot"]


#### Response:
status code: `204`

### Get instance information
`GET /instance/<region>/<instance_id>/`

#### Parameters:
- `api_key`: Api key for this app. Must be supplied as a header, or a cookie.
- `region`: Cannonical AWS region name. e.g. 'us-west-2'
- `instance_id`: AWS supplied instance id. e.g. 'i-abba916a'

#### Response:
status code: `200`

body:
```json
{
    "public_dns_name": "ec2-000-000-000-000.us-west-2.compute.amazonaws.com",
    "public_ip_address": "000.000.000.000",
    "state": "running",
    "tags": {
        "Name": "default",
        "start_time": "2016-02-16T18:04:09.006739"
    },
    "type": "t2.nano"
}
```

- `public_dns_name`: dns name given to the instance. value is released upon stopping instance.
- `public_ip_address`: public ip address given to instance. value is released upon stopping instance.
- `state`: current state of the instance,
- `tags`: tags given to the instance.
  - `Name`: Is set by giving the instance a name, otherwise, this value is absent. 
  - `start_time`: is set by workwork to keep track of how long the instance has been running. Value is an iso8601 formatted datetime string, and upon stopping the instance, the value is set to "".
- `type`: Instance size/type.


© Joeseph Rodrigues 2016
