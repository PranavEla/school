# -*- coding: utf-8 -*-
"""1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dzJzNMt0oVe26rLr4gNEa0fN6CthdoF8
"""

# Core Data Processing Libraries
import numpy as np
import pandas as pd
import json
import pickle
import re
import string
from collections import Counter, defaultdict
from tqdm import tqdm

# Basic NLP Libraries
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
from nltk.lm import MLE, KneserNeyInterpolated

# Advanced NLP Libraries
import spacy
from textblob import TextBlob
from gensim import corpora, models, similarities
from gensim.models import Word2Vec, FastText

# Text Processing and Cleaning
from bs4 import BeautifulSoup
import unicodedata
import html

# Machine Learning Libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline

# ML Algorithms
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# ML Metrics and Evaluation
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score
)

# Deep Learning Libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import (
    Dense, LSTM, GRU, Embedding, Dropout, BatchNormalization,
    Conv1D, MaxPooling1D, GlobalMaxPooling1D
)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Transformers and Advanced Models
from transformers import (
    AutoTokenizer, AutoModel, AutoModelForSequenceClassification,
    BertTokenizer, BertModel, BertForSequenceClassification,
    GPT2Tokenizer, GPT2LMHeadModel,
    T5Tokenizer, T5ForConditionalGeneration,
    DistilBertTokenizer, DistilBertForSequenceClassification
)

# Explainable AI
import lime
from lime import lime_text
import shap
from shap import KernelExplainer, TreeExplainer

# SVD and Matrix Operations
from sklearn.decomposition import TruncatedSVD, PCA, NMF
from scipy.sparse import csr_matrix, hstack, vstack
import scipy.stats as stats

# Image Processing (for SVD on images)
import cv2
from PIL import Image

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# BPE and Tokenization
from tokenizers import ByteLevelBPETokenizer, Tokenizer, BertWordPieceTokenizer

# Required NLTK downloads
nltk_resources = [
    'punkt',
    'stopwords',
    'wordnet',
    'averaged_perceptron_tagger',
    'vader_lexicon'
]

# Download NLTK resources
for resource in nltk_resources:
    try:
        nltk.download(resource, quiet=True)
    except:
        print(f"Failed to download {resource}")

# Initialize spaCy
try:
    nlp = spacy.load('en_core_web_sm')
except:
    print("Please install spaCy model using: python -m spacy download en_core_web_sm")

# Set random seeds for reproducibility
np.random.seed(42)
torch.manual_seed(42)
tf.random.set_seed(42)

# C - Convert to lowercase
# L - Letters only (remove special chars)
# E - Eliminate stopwords
# A - Analyze tokens
# N - Normalize (lemmatize/stem)
# U - Unite tokens
# P - Prepare for model

def preprocess_text(text):
    # C: Convert to lowercase
    text = text.lower()

    # L: Letters only (remove special chars & numbers)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # E: Eliminate stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]

    # A: Analyze tokens (here we just tokenize)
    # Already done in previous step

    # N: Normalize through lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    # U & P: Unite tokens and Prepare
    return ' '.join(tokens)

# Memory Tip: Think "CLEANUP" - like cleaning a messy text!

with open('filename.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('filename.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

with open('filename.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)

with open('filename.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())