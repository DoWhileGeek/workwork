import re
import subprocess

from setuptools import setup


def _get_git_description():
    try:
        return subprocess.check_output(["git", "describe"]).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None


def get_version():
    description = _get_git_description()

    match = re.match(r'(?P<tag>[\d\.]+)-(?P<offset>[\d]+)-(?P<sha>\w{8})', description)

    if match:
        version = "{tag}.post{offset}".format(**match.groupdict())
    else:
        version = description

    return version


def main():
    setup(
        name="workwork",
        url="https://github.com/DoWhileGeek/workwork",
        description="A flask api for managing aws ec2 instances",
        license="MIT License",
        author="Joeseph Rodrigues",
        author_email="dowhilegeek@gmail.com",
        version=get_version(),
        packages=["workwork", ],
        package_data={"workwork": ["workwork/*"], },
        include_package_data=True,
        install_requires=[
            "boto3==1.2.3",
            "Flask==0.10.1",
            "webargs==1.2.0",
        ],
        extras_require={
            "develop": [
                "pytest==2.8.7",
                "pytest-mock==0.6.0",
            ],
        },
    )


if __name__ == "__main__":
    main()
