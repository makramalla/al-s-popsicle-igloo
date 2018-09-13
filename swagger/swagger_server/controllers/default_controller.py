import connexion
import six

from swagger_server.models.store_schema import StoreSchema  # noqa: E501
from swagger_server import util


def create_store_by_id(store):  # noqa: E501
    """Create store by ID

    Create operation of resource: store # noqa: E501

    :param store: storebody object
    :type store: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        store = StoreSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_store_by_id():  # noqa: E501
    """Delete store by ID

    Delete operation of resource: store # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def retrieve_store():  # noqa: E501
    """Retrieve store

    Retrieve operation of resource: store # noqa: E501


    :rtype: StoreSchema
    """
    return 'do some magic!'


def update_store_by_id(store):  # noqa: E501
    """Update store by ID

    Update operation of resource: store # noqa: E501

    :param store: storebody object
    :type store: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        store = StoreSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
