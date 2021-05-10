import os
import re
import string
import pandas as pd

import nltk

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer
from textblob import TextBlob
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

from sklearn.model_selection import train_test_split

import plotly.express as px

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context





################### Setttings #############################
nltk.download('stopwords')
stopwords = stopwords.words('french')
root_path = os.path.dirname(os.path.realpath(__file__))
########################################################


###############################
# Dataset Cleaning
###############################

# Clean Review Body
def clean_review_body(rev):
    # Make text to lowerCase
    clean_rev = rev.lower()
    # Remove ponctuation like .,!? etc
    clean_rev = clean_rev.translate(str.maketrans('' ,'' ,string.punctuation))
    # Remove words that contain numbers
    clean_rev = re.sub(r'\w*\d\w*' ,'' ,clean_rev)
    return clean_rev

# Clean reviews DataFrame
def clean_reviews(df_rev):
    # Because NaN are those with (une personne a commenté )
    df_rev['Rev_Hlp'] = df_rev.Rev_Hlp.str.split(' ').apply(lambda x: 1 if x[0] == 'Une' else int(x[0]))

    # Cleaning Hlp Review
    # df_rev['Rev_Hlp'] = df_rev.Rev_Hlp.apply(lambda x: re.sub("[^0-9]" ,"" ,x))

    # Cleaning Rate review
    df_rev['Rev_Rate'] = df_rev.Rev_Rate.str.split(' ').apply(lambda x: float(x[0].replace(',' ,'.')))

    df_rev['Rev_Home'] = df_rev.Rev_Home.str.split(' ').apply(lambda x: x[2])

    # Cleaning the body of the review
    # Convert the letter into lowercase
    # Remove ponctuation like .,!? etc
    df_rev['Rev_Bdy'] = df_rev.Rev_Bdy.apply(lambda x: clean_review_body(x))

    df_rev = df_rev[df_rev.Rev_Home =='France']

    return df_rev
##############################################################

def clean_dataset():
    df_rev = pd.read_csv(os.path.join(root_path, '..', 'common', 'dataset.csv'))
    df_rev = clean_reviews(df_rev)
    ds = df_rev[df_rev["Rev_Home"] == 'France']
    ds = ds[["Rev_Title","Rev_Bdy"]]
    X = df_rev.copy()
    X = X.drop('Rev_Rate', axis=1)
    X = X.drop('Rev_Hlp', axis=1)
    X = X.drop('Rev_Home', axis=1)
    X = X.drop('Prod_ID', axis=1)
    return df_rev,ds,X

# Vectorization
def data_to_matrix(data):
  # Building the Victorizer
  stemmer = FrenchStemmer()
  analyzer = TfidfVectorizer().build_analyzer()
  vec = TfidfVectorizer(stop_words = stopwords,
                        analyzer = lambda doc:(stemmer.stem(w) for w in analyzer(doc)),
                        ngram_range = (1,3))
  # Build the new matrix dataset
  mx_rev = vec.fit_transform(data.Rev_Bdy)
  df_rev = pd.DataFrame(mx_rev.toarray(),columns = vec.get_feature_names())
  df_rev.index = data.index
  df_rev.insert(0, 'Title', data.Rev_Title)
  return df_rev
####################### END Vectorization ########################


##################### Sentiment Analysis ########################

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

# To exctract polarity from a message **msg
def get_polarity(msg):
    return tb(str(msg)).sentiment[0]


# To exctract subjectivity from a message **msg
def get_subjectivity(msg):
    return tb(str(msg)).sentiment[1]


def encode_sentiment(sentiment):
    if sentiment == 'Positive':
        return 1
    elif sentiment == 'Negative':
        return -1
    else:
        return 0


def decode_sentiment(data):
    if data > 0:
        return 'Positive'
    elif data < 0:
        return 'Negative'
    else:
        return 'Neutral'


def add_sub_pol_to_dataset(ds):
    ds['Subjectivity'] = ds['Rev_Bdy'].apply(get_subjectivity)
    ds['Polarity'] = ds['Rev_Bdy'].apply(get_polarity)
    ds['Sentiment'] = ds['Polarity'].apply(decode_sentiment)
    return ds


def dataset_merge():
    ds_path = os.path.join(root_path, '..', 'common', 'dataset.csv')
    ds1_path = os.path.join(root_path, '..', 'common', 'reviews_dataset.csv')
    ds2_path = os.path.join(root_path, '..', 'common', 'reviews_dataset_1.csv')
    ds1 = pd.read_csv(ds1_path)
    ds2 = pd.read_csv(ds2_path)
    ds2['Prod_ID'] = ds2['Prod_ID'].map(lambda x : 20 if x == 10 else x)
    frames = [ds1,ds2]
    ds = pd.concat(frames)
    ds.reset_index(drop=True,inplace=True)
    ds.to_csv(ds_path,index=False)
    return ds

def save_dataset(ds):
    ds_path = os.path.join(root_path, '..', 'common', 'clean_dataset.csv')
    ds.to_csv(ds_path,index=False)



if __name__ == '__main__':

    df_rev, ds, X = clean_dataset()


    mx_rev = data_to_matrix(X)
    ds = add_sub_pol_to_dataset(ds)
    y = ds['Sentiment'].apply(encode_sentiment)
    mx_rev = mx_rev.drop('Title',axis = 1)

    X_train , X_test , y_train , y_test = train_test_split(mx_rev,y,test_size = 0.2)

    X_train.to_csv(os.path.join(root_path,'..','common','X_train.csv'),index=False)
    X_test.to_csv(os.path.join(root_path,'..','common','X_test.csv'),index=False)
    y_train.to_csv(os.path.join(root_path,'..','common','y_train.csv'),index=False)
    y_test.to_csv(os.path.join(root_path,'..','common','y_test.csv'),index=False)

