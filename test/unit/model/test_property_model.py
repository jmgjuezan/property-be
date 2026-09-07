import app.model.property_model as property_model
import mongomock
import pytest

name_1 = "property test 1"
name_2 = "property test 2"
test_property = {
    "name": name_1,
}


@pytest.fixture
def mock_collection(monkeypatch):
    client = mongomock.MongoClient()
    db = client["prop-mgmt"]
    collection = db[property_model.table]

    monkeypatch.setattr(
        property_model,
        "collection",
        collection,
    )

    return collection


def test_delete_property(mock_collection):
    result = mock_collection.insert_one(test_property)
    property_model.delete(result.inserted_id)
    property = mock_collection.find_one(result.inserted_id)
    assert property is not None
    assert property["name"] == name_1
    assert property["deleted"] is True


def test_read_properties(mock_collection):
    mock_collection.insert_one(test_property)
    new_test_property = {"name": name_2}
    mock_collection.insert_one(new_test_property)
    properties = property_model.find_all()
    assert properties is not None
    assert len(properties) == 2
    assert properties[0]["name"] == name_1
    assert properties[1]["name"] == name_2


def test_read_property(mock_collection):
    result = mock_collection.insert_one(test_property)
    property = property_model.find_one(result.inserted_id)
    assert property is not None
    assert property["name"] == name_1


def test_save_property(mock_collection):
    result = property_model.save(test_property)
    assert result is not None
    assert result.inserted_id is not None
    property = mock_collection.find_one(result.inserted_id)
    assert property is not None
    assert property["name"] == name_1
    assert property["_id"] == result.inserted_id


def test_update_property(mock_collection):
    result = mock_collection.insert_one(test_property)
    new_test_property = test_property.copy()
    new_test_property["name"] = name_2
    property_model.update(result.inserted_id, new_test_property)
    property = mock_collection.find_one(result.inserted_id)
    assert property is not None
    assert property["name"] == name_2
    assert property["_id"] == result.inserted_id
