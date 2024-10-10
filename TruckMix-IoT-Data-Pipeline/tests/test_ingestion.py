import pytest

from src.ingestion.data_ingestion import ingest_data  # Adjust the import path based on your project structure

@pytest.fixture
def sample_data():
    return {
        "truck_id": "1234",
        "timestamp": "2023-10-01T12:00:00Z",
        "sensor_data": {
            "temperature": 25.5,
            "humidity": 60,
            "vibration": 0.02
        }
    }

def test_ingest_data_success(sample_data):
    result = ingest_data(sample_data)
    assert result == "Data ingested successfully"

def test_ingest_data_missing_truck_id(sample_data):
    del sample_data["truck_id"]
    with pytest.raises(KeyError):
        ingest_data(sample_data)

def test_ingest_data_invalid_timestamp(sample_data):
    sample_data["timestamp"] = "invalid-timestamp"
    with pytest.raises(ValueError):
        ingest_data(sample_data)

def test_ingest_data_missing_sensor_data(sample_data):
    del sample_data["sensor_data"]
    with pytest.raises(KeyError):
        ingest_data(sample_data)