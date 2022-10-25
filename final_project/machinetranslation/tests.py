import unittest
import translator as translate

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(translate.english_to_french(' '),'Salut')
        self.assertEqual(translate.english_to_french('Hello'),'Bonjour')
        
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(translate.french_to_english(' '),'How are you')
        self.assertEqual(translate.french_to_english('Bonjour'),'Hello')
        
unittest.main()