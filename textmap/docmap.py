import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin
from vectorizers import NgramVectorizer

from sklearn.utils.validation import check_X_y, check_array, check_is_fitted


class DocMAP(BaseEstimator, TransformerMixin):
    """
    Doc2Vec replacement
    """

    pass


class TopicMAP(BaseEstimator, TransformerMixin):
    """
    LDA replacement
    Joint word/document embedding.
    Topics are points in joint word/document space.
    Topics have co-ordinates and descriptions (weighted sets of words learned from the fit).
    """

    def __init__(self):

        pass

    def fit(self):
        """
        Call DocMAP.fit() with joint=True
        UMAP + hdbscan
        create topics from weighted hdbscan centroids.
        Saves a weighted word list for each topic
        :return:
        """
        pass

    def transform(self):
        """
        Takes a document or collection of documents
        DocMAP.transform() to give high space representation
        Hellinger is what is the difference between my topic model and the distribution most likely to generate my set
        of observations.
        Hellinger distance says that my documents, words and topics are the maximum likelyhood estimate models for the
        observed counts.

        LDA does this differently, it returns the vector of likelyhoods of each document being generated by each
        multinomial.  Likelyhood is what is the likelihood of these observations being generated by my topic
        distribution.  We don't treat a document as a set of observations we treat is as the the model.
        :return:
        """
        pass

    pass
