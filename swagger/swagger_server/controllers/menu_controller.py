import connexion
import six

from swagger_server.models.popsicles_data import PopsiclesData  # noqa: E501
from swagger_server import util


def retrieve_menu():  # noqa: E501
    """Retrieve menu

    Retrieve operation of resource: menu # noqa: E501


    :rtype: List[str]
    """
    result = [
        {"menu_item": "green popsicle", "price": 1.50, "description": "A green popsicle", "type": "sweet"},
        {"menu_item": "sour green popsicle", "price": 1.50, "description": "A green popsicle", "type": "sour"},
        {"menu_item": "blue popsicle", "price": 1.50, "description": "A green popsicle", "type": "sweet"},
        {"menu_item": "rainbow popsicle", "price": 2.50, "description": "A rainbow popsicle", "type": "sweet"},
        {"menu_item": "clown bubblegum popsicle", "price": 5.50, "description": "A clown popsicle with a bubblegum nose", "type": "sweet"}
    ]
    return result


def retrieve_menu_menu_by_id(menu_item):  # noqa: E501
    """Retrieve menu by ID

    Retrieve operation of resource: menu # noqa: E501

    :param menu_item: ID of menu_item
    :type menu_item: str

    :rtype: PopsiclesData
    """
    menu_items = [
        {"menu_item": "green popsicle", "price": 1.50, "description": "A green popsicle", "type": "sweet"},
        {"menu_item": "sour green popsicle", "price": 1.50, "description": "A green popsicle", "type": "sour"},
        {"menu_item": "blue popsicle", "price": 1.50, "description": "A green popsicle", "type": "sweet"},
        {"menu_item": "rainbow popsicle", "price": 2.50, "description": "A rainbow popsicle", "type": "sweet"},
        {"menu_item": "clown bubblegum popsicle", "price": 5.50, "description": "A clown popsicle with a bubblegum nose", "type": "sweet"}
    ]
    for item in menu_items:
        if item['menu_item'] == menu_item:
            return item
    return "Sorry. We don't have %s" % menu_item
