"""Constants for the Jablotron Cloud integration."""

from homeassistant.backports.enum import StrEnum

DOMAIN = "jablotron_cloud"

SERVICE_ID = "service-id"
SERVICE_TYPE = "service-type"

PG_ID = "cloud-component-id"
PG_STATE = "state"
PG_STATE_OFF = "OFF"


class Actions(StrEnum):
    """Actions to control sections."""

    ARM = "ARM"
    DISARM = "DISARM"
    PARTIAL_ARM = "PARTIAL_ARM"
