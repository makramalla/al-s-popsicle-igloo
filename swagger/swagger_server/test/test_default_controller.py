# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.store_schema import StoreSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_store_by_id(self):
        """Test case for create_store_by_id

        Create store by ID
        """
        store = StoreSchema()
        response = self.client.open(
            '/restconf/config/store/',
            method='POST',
            data=json.dumps(store),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_store_by_id(self):
        """Test case for delete_store_by_id

        Delete store by ID
        """
        response = self.client.open(
            '/restconf/config/store/',
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_store(self):
        """Test case for retrieve_store

        Retrieve store
        """
        response = self.client.open(
            '/restconf/config/store/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_store_by_id(self):
        """Test case for update_store_by_id

        Update store by ID
        """
        store = StoreSchema()
        response = self.client.open(
            '/restconf/config/store/',
            method='PUT',
            data=json.dumps(store),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
