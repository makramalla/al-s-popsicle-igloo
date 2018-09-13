import connexion
import six

from swagger_server.models.purchase_response_schema import PurchaseResponseSchema  # noqa: E501
from swagger_server.models.purchase_schema import PurchaseSchema  # noqa: E501
from swagger_server import util


def create_purchase_purchase_by_id(purchase):  # noqa: E501
    """Create purchase by ID

    Create operation of resource: purchase # noqa: E501

    :param purchase: purchasebody object
    :type purchase: dict | bytes

    :rtype: PurchaseResponseSchema
    """
    if connexion.request.is_json:
        purchase = PurchaseSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def retrieve_purchase():  # noqa: E501
    """Retrieve purchase

    Retrieve operation of resource: purchase # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_purchase_purchase_by_id(uuid):  # noqa: E501
    """Retrieve purchase by ID

    Retrieve operation of resource: purchase # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: PurchaseSchema
    """
    return 'do some magic!'
