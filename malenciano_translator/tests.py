import unittest
import translators
from translate import getPhraseTranslated
from words.word import Word
from words.short_word import ShortWord

class TestTraduction(unittest.TestCase):

    castellan1 = "bocadillo de jamón y queso"
    valencian1 = "bocadill de jamó i ques"

    translator = translators.Translator(castellan1)

    def testWordsAreNotEqual(self):
        self.assertNotEqual(self.castellan1, self.valencian1)
    
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
        self.assertEqual(self.valencian1, getPhraseTranslated(self.castellan1))

    def testBocadilloPhrase(self):
        self.assertEqual(self.valencian1, self.translator.translate())

    def testYaSeHaAcabadoPhrase(self):
        castellan2 = "Ya se ha acabado"
        valencian2 = "Ya se ha acabat"
        translator2 = translators.Translator(castellan2)
        self.assertEqual(valencian2, translator2.translate())   

    def testEstamosLocosPhrase(self):
        castellan3 = "Estamos locos"
        valencian3 = "Estem locs"    
        translator3 = translators.Translator(castellan3)
        self.assertEqual(valencian3, translator3.translate())   

    def testTomateConPepino(self):
        castellan4 = "Tomate con pepino"
        valencian4 = "Tomat amb pepin"    
        translator4 = translators.Translator(castellan4)
        self.assertEqual(valencian4, translator4.translate())

    def testOjoCuidado(self):
        castellan5 = "Ojo cuidado"
        valencian5 = "Oj cuidat"    
        translator5 = translators.Translator(castellan5)
        self.assertEqual(valencian5, translator5.translate())        

    def testOlivasSinHueso(self):
        castellan6 = "Olivas sin hueso"
        valencian6 = "Olives sin hues"    
        translator6 = translators.Translator(castellan6)
        self.assertEqual(valencian6, translator6.translate())   

    def testMeHasMatadoConEso(self):
        castellan7 = "Me has matado con eso"
        valencian7 = "Me has matat amb es"    
        translator7 = translators.Translator(castellan7)
        self.assertEqual(valencian7, translator7.translate())

    def testNotTranslateMention(self):
        castellan8 = "Oye @queso quiero un bocadillo de queso"
        valencian8 = "Oy @queso quier un bocadill de ques"    
        translator8 = translators.Translator(castellan8)
        self.assertEqual(valencian8, translator8.translate())               

if __name__ == "__main__":
    unittest.main()