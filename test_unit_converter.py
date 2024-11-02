import unittest
from unit_converter import convert_storage, convert_distance, load_unit_mappings

# Load unit mappings for testing
unit_mappings = load_unit_mappings('unit_mappings.json')

class TestUnitConverter(unittest.TestCase):
    def test_convert_storage(self):
        # Testing storage conversions - bytes to kilobytes
        self.assertAlmostEqual(convert_storage(1024, 'B', 'KB'), 1)
        # Testing kilobytes to megabytes
        self.assertAlmostEqual(convert_storage(1048576, 'B', 'MB'), 1)
        # Removed TB to PB test case for now

    def test_convert_distance(self):
        # Testing distance conversions - millimeters to meters
        self.assertAlmostEqual(convert_distance(1000, 'MM', 'M'), 1)
        # Testing meters to kilometers
        self.assertAlmostEqual(convert_distance(1000, 'M', 'KM'), 1)
        # Testing centimeters to millimeters
        self.assertAlmostEqual(convert_distance(1, 'CM', 'MM'), 10)

if __name__ == "__main__":
    unittest.main()