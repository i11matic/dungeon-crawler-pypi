from dungeon_crawler import __version__
from dungeon_crawler import Item


def test_version():
    assert __version__ == "0.1.0"


def test_item_creation():
    test_item = Item(
        name="dummy_item", description="dummy_description", value="dummy_value"
    )
    assert test_item.__dict__ == {
        "name": "dummy_item",
        "description": "dummy_description",
        "value": "dummy_value",
    }