import unittest
import translator

class TestFr2EnMethod(unittest.TestCase):
    def test_translateBonjour(self):
        frenchText = 'Bonjour'
        transatedText = translator.french_to_english(frenchText)
        self.assertEquals(transatedText, "Hello")

    def test_translateHello(self):
        frenchText = 'Hello'
        transatedText = translator.french_to_english(frenchText)
        self.assertEquals(transatedText, "Hello")

    def test_translateNull(self):
        frenchText = ''
        with self.assertRaises(Exception):
            translator.french_to_english(frenchText)

class TestEn2FrMethod(unittest.TestCase):
    def test_translateBonjour(self):
        frenchText = 'Bonjour'
        transatedText = translator.english_to_french(frenchText)
        self.assertEquals(transatedText, "Bonjour")

    def test_translateHello(self):
        frenchText = 'Hello'
        transatedText = translator.english_to_french(frenchText)
        self.assertEquals(transatedText, "Bonjour")

    def test_translateNull(self):
        frenchText = ''
        with self.assertRaises(Exception):
            translator.english_to_french(frenchText)
        

if __name__ == '__main__':
    unittest.main()