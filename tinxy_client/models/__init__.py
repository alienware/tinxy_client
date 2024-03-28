# coding: utf-8

# flake8: noqa
"""
    Tinxy API Documentation

    ### Steps    1. Install the Tinxy Mobile application    2. Login to application    3. Click on the setting icon (top left on android)    4. Click on API Token    5. Click on Get to token     6. Copy and save toke for usage in api  ## Notes Token should be sent via `Authorization: Bearer <token here>` header  

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from tinxy_client.models.device import Device
from tinxy_client.models.device_state import DeviceState
from tinxy_client.models.toggle import Toggle
from tinxy_client.models.toggle_request import ToggleRequest
from tinxy_client.models.toggle_response import ToggleResponse
from tinxy_client.models.type_id import TypeId
