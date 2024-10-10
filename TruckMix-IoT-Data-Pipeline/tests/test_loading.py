import unittest
from src.pipeline.etl_pipeline import load_data

class TestLoading(unittest.TestCase):

    def setUp(self):
        # Setup code if needed
        self.valid_data = {
            'id': 1,
            'timestamp': '2023-10-01T12:00:00Z',
            'sensor_data': {
                'temperature': 25.5,
                'humidity': 40.0
            }
        }
        self.invalid_data = {
            'id': 'invalid_id',
            'timestamp': 'invalid_timestamp',
            'sensor_data': {
                'temperature': 'invalid_temp',
                'humidity': 'invalid_humidity'
            }
        }

    def test_load_valid_data(self):
        result = load_data(self.valid_data)
        self.assertTrue(result)
        # Add more assertions based on what load_data returns

    def test_load_invalid_data(self):
        with self.assertRaises(ValueError):
            load_data(self.invalid_data)
        # Add more assertions based on what load_data should raise

    def test_load_empty_data(self):
        with self.assertRaises(ValueError):
            load_data({})
        # Add more assertions based on what load_data should raise

    def test_load_partial_data(self):
        partial_data = {
            'id': 1,
            'timestamp': '2023-10-01T12:00:00Z'
            # Missing sensor_data
        }
        with self.assertRaises(KeyError):
            load_data(partial_data)
        # Add more assertions based on what load_data should raise

if __name__ == '__main__':
    unittest.main()