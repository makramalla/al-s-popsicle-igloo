# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.purchase_response_schema import PurchaseResponseSchema  # noqa: E501
from swagger_server.models.purchase_schema import PurchaseSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPurchaseController(BaseTestCase):
    """PurchaseController integration test stubs"""

    def test_create_purchase_purchase_by_id(self):
        """Test case for create_purchase_purchase_by_id

        Create purchase by ID
        """
        purchase = PurchaseSchema()
        response = self.client.open(
            '/restconf/config/purchase/',
            method='POST',
            data=json.dumps(purchase),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_purchase(self):
        """Test case for retrieve_purchase

        Retrieve purchase
        """
        response = self.client.open(
            '/restconf/config/purchase/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_purchase_purchase_by_id(self):
        """Test case for retrieve_purchase_purchase_by_id

        Retrieve purchase by ID
        """
        response = self.client.open(
            '/restconf/config/purchase/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
