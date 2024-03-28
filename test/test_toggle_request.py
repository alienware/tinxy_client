# coding: utf-8

"""
    Tinxy API Documentation

    ### Steps    1. Install the Tinxy Mobile application    2. Login to application    3. Click on the setting icon (top left on android)    4. Click on API Token    5. Click on Get to token     6. Copy and save toke for usage in api  ## Notes Token should be sent via `Authorization: Bearer <token here>` header  

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tinxy_client.models.toggle_request import ToggleRequest

class TestToggleRequest(unittest.TestCase):
    """ToggleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ToggleRequest:
        """Test ToggleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ToggleRequest`
        """
        model = ToggleRequest()
        if include_optional:
            return ToggleRequest(
                state = 1,
                brightness = 33
            )
        else:
            return ToggleRequest(
        )
        """

    def testToggleRequest(self):
        """Test ToggleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
