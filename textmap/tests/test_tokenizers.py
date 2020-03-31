import pytest

import spacy
from spacy.lang.en import English
# import stanza

from textmap.tokenizers import (
    SpaCyTokenizer,
    NLTKTokenizer,
    NLTKTweetTokenizer,
    SKLearnTokenizer,
    StanzaTokenizer,
)
from .test_common import test_text


def test_sklearn_tokenizer():
    for tokens_by in ["document", "sentence"]:
        tokenizer = SKLearnTokenizer(tokenize_by=tokens_by).fit(test_text)


def test_nltk_tokenizer():
    for tokens_by in ["document", "sentence"]:
        tokenizer = NLTKTokenizer(tokenize_by=tokens_by).fit(test_text)


def test_tweet_tokenizer():
    for tokens_by in ["document", "sentence"]:
        tokenizer = NLTKTweetTokenizer(tokenize_by=tokens_by).fit(test_text)


def test_spacy_tokenizer():
    for tokens_by in ["document", "sentence"]:
        tokenizer = SpaCyTokenizer(tokenize_by=tokens_by).fit(test_text)


def test_spacy_add_sentencizer():
    nlp = English()
    # Remove all of the components
    for p in nlp.pipe_names:
        nlp.remove_pipe(p)
    tokenizer = SpaCyTokenizer(tokenize_by="sentence", nlp=nlp)
    assert "sentencizer" in tokenizer.nlp.pipe_names


def test_spacy_remove_sentencizer():
    nlp = English()
    nlp.add_pipe(nlp.create_pipe("sentencizer"), first=True)
    tokenizer = SpaCyTokenizer(tokenize_by="document", nlp=nlp)
    assert not ("sentencizer" in tokenizer.nlp.pipe_names)

'''

Stanza requires PyTorch which isn't behaving well in the github testing (the tests did pass locally though)  

def test_stanza_tokenizer():
    for tokens_by in ["document", "sentence"]:
        tokenizer = StanzaTokenizer(tokenize_by=tokens_by).fit(test_text)


def test_stanza_add_sentencizer():
    stanza.download(lang="en", processors="tokenize")
    nlp = stanza.Pipeline(processors="tokenize", tokenize_no_ssplit=True)
    tokenizer = StanzaTokenizer(tokenize_by="sentence", nlp=nlp)
    assert not tokenizer.nlp.config["tokenize_no_ssplit"]


def test_stanza_remove_sentencizer():
    stanza.download(lang="en", processors="tokenize")
    nlp = stanza.Pipeline(processors="tokenize", tokenize_no_ssplit=False)
    tokenizer = StanzaTokenizer(tokenize_by="document", nlp=nlp)
    assert tokenizer.nlp.config["tokenize_no_ssplit"]
'''