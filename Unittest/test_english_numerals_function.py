import unittest
from numerals import integer_to_english_numeral


class EnglishNumeralsTestCase(unittest.TestCase):
    """Test for integer_to_english_numeral function."""

    def test_numerals(self):
        dict_number = {96: 'ninety-six', 101: 'one hundred and one',
                       405: 'four hundred and five',
                       1971: 'one thousand and nine hundred and seventy-one',
                       5061: 'five thousand and sixty-one'}
        for key, value in dict_number.items():
            self.assertEqual(integer_to_english_numeral(key), value)


if __name__ == '__main__':
    unittest.main()
