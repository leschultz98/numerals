import unittest
from numerals import integer_to_vietnamese_numeral


class VietnameseNumeralsTestCase(unittest.TestCase):
    """Test for integer_to_vietnamese_numeral function."""

    def test_north_numerals(self):
        dict_number = {96: 'chín mươi sáu', 405: 'bốn trăm linh năm',
                       1915: 'một nghìn chín trăm mười lăm',
                       5061: 'năm nghìn không trăm sáu mươi mốt',
                       1002003: 'một triệu không trăm linh hai nghìn không trăm linh ba',
                       1000000: 'một triệu',
                       1030000: 'một triệu không trăm ba mươi nghìn',
                       1002003004: 'một tỷ không trăm linh hai triệu không trăm linh ba nghìn không trăm linh bốn',
                       1002000004: 'một tỷ không trăm linh hai triệu không trăm linh bốn',
                       100000004: 'một trăm triệu không trăm linh bốn',
                       999999999999: 'chín trăm chín mươi chín tỷ chín trăm chín mươi chín triệu chín trăm chín mươi chín nghìn chín trăm chín mươi chín'}

    def test_south_numerals(self):
        dict_number = {96: 'chín mươi sáu', 405: 'bốn trăm lẻ năm',
                       1915: 'một ngàn chín trăm mười lăm',
                       5061: 'năm ngàn không trăm sáu mươi mốt',
                       1002003: 'một triệu không trăm lẻ hai ngàn không trăm lẻ ba',
                       1000000: 'một triệu',
                       1030000: 'một triệu không trăm ba mươi ngàn',
                       1002003004: 'một tỷ không trăm lẻ hai triệu không trăm lẻ ba ngàn không trăm lẻ bốn',
                       1002000004: 'một tỷ không trăm lẻ hai triệu không trăm lẻ bốn',
                       100000004: 'một trăm triệu không trăm lẻ bốn',
                       999999999999: 'chín trăm chín mươi chín tỷ chín trăm chín mươi chín triệu chín trăm chín mươi chín ngàn chín trăm chín mươi chín'}
        for key, value in dict_number.items():
            self.assertEqual(integer_to_vietnamese_numeral(key, 'south'),
                             value)


if __name__ == '__main__':
    unittest.main()
