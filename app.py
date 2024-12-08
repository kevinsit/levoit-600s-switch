import os
import datetime
import logging
import click

from dotenv import load_dotenv
from pyvesync import VeSync

logger = logging.getLogger(__name__)

load_dotenv()

email = os.getenv("VESYNC_EMAIL")
password = os.getenv("VESYNC_PASSWORD")

now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)

tz = os.getenv("VESYNC_TIMEZONE", local_tzname)


@click.group()
def cli():
    """Air Purifier controller."""
    pass


@cli.command()
@click.argument('state')
def purifiers(state):
    """Control Air Purifiers"""
    manager = get_manager()
    for device in manager.fans:
        if state == "on":
            logger.info("Turn on purifier: %s", device.device_name)
            device.turn_on()
        elif state == "off":
            logger.info("Turn off purifier: %s", device.device_name)
            device.turn_off()


def get_manager():
    manager = VeSync(email, password, tz, debug=False, redact=True)
    manager.login()
    manager.update()
    return manager


if __name__ == '__main__':
    cli()
