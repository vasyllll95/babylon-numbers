import unittest
import genty
import babylon.babylon_number_packager as babylon_packager


@genty.genty
class TestBabylonPackageNumber(unittest.TestCase):

    @genty.genty_dataset(
        (10, "<", "10 value is not converted correctly"),
        (11, "<Y", "10 value is not converted correctly"),
        (0, "", "0 value is not converted correctly"),
        (2, "YY", "2 value is not converted correctly")
        )
    def test_package_number(self,actual_number, expected_number, message):
        self.assertEqual(babylon_packager.package_number_to_babylon(actual_number), expected_number, message)

if __name__=='__main__':
    unittest.main()