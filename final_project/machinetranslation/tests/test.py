import unittest
from ..translator import english_to_french, french_to_english

class TestStringMethods(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        with self.assertRaises(TypeError):
            english_to_french()

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        with self.assertRaises(TypeError):
            french_to_english()

if __name__ == '__main__':
    unittest.main()