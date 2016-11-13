# -*- coding: cp1252 -*-
#my_utility

from os import listdir
from os.path import isfile,join

from nltk.corpus import stopwords
import string
from tokenizer import preprocess

import math
from textblob import TextBlob as tb

import json
import sys

import operator
from collections import Counter



def get_single_line_token(line):
    words=[]
    words+=line.split()
    return words

def text_from_json(e_json):
    test=json.loads(e_json)
    
    text=test['text'].lower()
    #print test['id']
    text=text.encode('ascii','ignore')
    return text

#ricrea un unica stringa
def assemble_tweet_giornaliero(token):
    tweet=" "
    return (tweet.join(token))

def parse_tweet_file(file_name):
    with open(file_name,'r') as f:
        token_file=[]
        for line in f:
            text=text_from_json(line) #estrare il campo text dal tweet in json
            text=preprocess(text) #rimuove le stop words
            text=my_filter(text)
            text=assemble_tweet_giornaliero(text) #riassembla il tweet ma questa volta senza stopword
            #print text
            token_file.append(text)
            #print text
        return token_file

def parse_tweet_file_single(file_name):
    with open(file_name,'r') as f:
        token_file=[]
        for line in f:
            text=text_from_json(line) #estrare il campo text dal tweet in json
            text=preprocess(text) #rimuove le stop words
            text=my_filter(text)
            text=assemble_tweet_giornaliero(text) #riassembla il tweet ma questa volta senza stopword
            token_file.append(text)
        return token_file


def my_filter(token):
    punctuation = list(string.punctuation)
    articoli=['il','lo','la','i','gli','le']
    common=['più','meno','fa','pi','si','no','va','poi','dopo','mai','prima','dice','due','aver','ecco','grande','piccolo','grandi','piccoli','ora','solo','essere','ieri','domani','wi-fi','sci-fi','to','new','sempre','by','me','ht','at','oggi','c\'era']
    single=['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z','j','k','y','z','1','2','3','4','5','6','7','8','9','0']
    stop = stopwords.words('italian') + punctuation + ['rt', 'via']+articoli+single+common

    term_all=[term for term in token if term not in stop and not term.startswith(("htt","#","@"))]
    return term_all

def find_corpus(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
