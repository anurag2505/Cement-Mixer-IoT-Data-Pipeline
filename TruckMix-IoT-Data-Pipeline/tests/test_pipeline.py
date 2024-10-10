import unittest
from pipeline import process_data, validate_data, transform_data

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            'sensor_id': '12345',
            'timestamp': '2023-10-01T12:00:00Z',
            'temperature': 25.5,
            'humidity': 40.0,
            'vibration': 0.02
        }

    def test_validate_data(self):
        valid_data = validate_data(self.sample_data)
        self.assertTrue(valid_data)

    def test_transform_data(self):
        transformed_data = transform_data(self.sample_data)
        self.assertIn('sensor_id', transformed_data)
        self.assertIn('timestamp', transformed_data)
        self.assertIn('temperature', transformed_data)
        self.assertIn('humidity', transformed_data)
        self.assertIn('vibration', transformed_data)

    def test_process_data(self):
        processed_data = process_data(self.sample_data)
        self.assertIsNotNone(processed_data)
        self.assertIn('sensor_id', processed_data)
        self.assertIn('timestamp', processed_data)
        self.assertIn('temperature', processed_data)
        self.assertIn('humidity', processed_data)
        self.assertIn('vibration', processed_data)

if __name__ == '__main__':
    unittest.main()