import sentences1
import sentences2
from sentences1 import *
from unittest import TestCase


class TestSentencesFunction(TestCase):
    def test_sentences(self):
        sentences = "Hello world! 123"
        self.assertEqual("LETTERS 3 DIGIT 10", sentences1.count(sentences))

    def test_sentences1(self):
        sentences = "Hello world!"
        self.assertEqual("UPPER CASE 1 LOWER CASE 9", sentences2.count(sentences))
