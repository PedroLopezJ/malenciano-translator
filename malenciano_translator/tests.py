import unittest
from malenciano_translator.translators import Translator
from malenciano_translator.words.word import Word
from malenciano_translator.__main__ import getPhraseTranslated

class TestTraduction(unittest.TestCase):

    castellan = "bocadillo de jamón y queso"
    valencian = "bocadill de jamó i ques"

    translator = Translator(castellan)

    def testWordsAreNotEqual(self):
        self.assertNotEqual(self.castellan, self.valencian)
    
    def testLongWordIsTrue(self):
        testWord = Word("esternocleidomastoideo")
        self.assertTrue(testWord.isLong())

    def testIsMention(self):
        testWord = Word("@name")
        self.assertTrue(testWord.isMention())

    def testShortWordIsFalse(self):
        testWord = Word("si")
        self.assertFalse(testWord.isLong())  

    def testYreplacements(self):
        self.assertEqual("i", self.translator.processWord("y")) 
        self.assertEqual("i,", self.translator.processWord("y,"))           
        self.assertNotEqual("r,", self.translator.processWord("y,"))
        self.assertNotEqual("ir,", self.translator.processWord("y,"))   

    def testGetPhraseTranslatedFromMain(self):
        self.assertEqual(self.valencian, getPhraseTranslated(self.castellan))

    def testBocadilloPhrase(self):
        self.assertEqual(self.valencian, self.translator.translate())

    def testYaSeHaAcabadoPhrase(self):
        castellan = "Ya se ha acabado"
        valencian = "Ya se ha acabat"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testEstamosLocosPhrase(self):
        castellan = "Estamos locos"
        valencian = "Estem locs"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testTomateConPepino(self):
        castellan = "Tomate con pepino"
        valencian = "Tomat amb pepin"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testOjoCuidado(self):
        castellan = "Ojo cuidado"
        valencian = "Oj cuidat"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testOlivasSinHueso(self):
        castellan = "Olivas sin hueso"
        valencian = "Olives sin hues"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testMeHasMatadoConEso(self):
        castellan = "Me has matado con eso"
        valencian = "Me has matat amb es"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testNotTranslateMention(self):
        castellan = "Oye @queso quiero un bocadillo de queso"
        valencian = "Oy @queso quier un bocadill de ques"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testNotTranslateMention(self):
        castellan = "Voy a ir mañana"
        valencian = "Voy a ir manyan"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

    def testNotTranslateMention(self):
        castellan = "A @persona le van a gustar los traductores"
        valencian = "A @persona li van a gust els traductors"
        translator = Translator(castellan)
        self.assertEqual(valencian, translator.translate())

if __name__ == "__main__":
    unittest.main()