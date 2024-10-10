import unittest
import numpy as np

def transform_data(data):
    # Placeholder for the actual transformation logic
    return np.convolve(data, np.ones(3)/3, mode='valid')

class TestTransformation(unittest.TestCase):

    def test_transformation_smoothness(self):
        input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        transformed_data = transform_data(input_data)
        
        # Check if the transformed data is smoother than the input data
        input_variance = np.var(input_data)
        transformed_variance = np.var(transformed_data)
        
        self.assertLess(transformed_variance, input_variance, "Transformed data is not smoother than input data")

    def test_transformation_output_length(self):
        input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        transformed_data = transform_data(input_data)
        
        # Check if the length of the transformed data is as expected
        expected_length = len(input_data) - 2  # Adjust based on the transformation logic
        self.assertEqual(len(transformed_data), expected_length, "Transformed data length is not as expected")

if __name__ == '__main__':
    unittest.main()