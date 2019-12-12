import unittest


from tse_data_reader.utils import normalize_persian_chars


class TestData(unittest.TestCase):
    def test_cleaner(self):
        string = "اصلاح كاف و ياي عربي"
        test = normalize_persian_chars(string)
        self.assertEqual(test, "اصلاح کاف و یای عربی")
