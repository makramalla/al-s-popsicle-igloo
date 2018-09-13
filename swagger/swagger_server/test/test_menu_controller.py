# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.popsicles_data import PopsiclesData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMenuController(BaseTestCase):
    """MenuController integration test stubs"""

    def test_retrieve_menu(self):
        """Test case for retrieve_menu

        Retrieve menu
        """
        response = self.client.open(
            '/restconf/config/menu/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_menu_menu_by_id(self):
        """Test case for retrieve_menu_menu_by_id

        Retrieve menu by ID
        """
        response = self.client.open(
            '/restconf/config/menu/{menu_item}/'.format(menu_item='menu_item_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
