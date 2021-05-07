import os
import pandas as pd
import streamlit as st

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

root_path = os.path.dirname(os.path.realpath(__file__))
X_train_path = os.path.join(root_path, '..', 'common', 'X_train.csv')
X_test_path = os.path.join(root_path, '..', 'common', 'X_test.csv')
y_train_path = os.path.join(root_path, '..', 'common', 'y_train.csv')
y_test_path = os.path.join(root_path, '..', 'common', 'y_test.csv')


@st.cache
def load_data():
    X_train = pd.read_csv(X_train_path)
    X_test = pd.read_csv(X_test_path)
    y_train = pd.read_csv(y_train_path)
    y_test = pd.read_csv(y_test_path)
    return X_train[:300],X_test[:200],y_train[:300],y_test[:200]


@st.cache
def train_svm(kernel,degree,C,gamma,decision_function):
    X_train, X_test, y_train, y_test = load_data()
    svm = SVC(kernel=kernel,degree=degree, C=C,gamma=gamma, decision_function_shape=decision_function)
    svm.fit(X_train, y_train)
    return svm.score(X_test,y_test)


@st.cache
def train_knn(n_neighbors,weights='uniform',metric='minkowski'):
    X_train, X_test, y_train, y_test = load_data()
    knn = KNeighborsClassifier(n_neighbors=n_neighbors,weights=weights, metric=metric)
    knn.fit(X_train, y_train)
    return knn.score(X_test,y_test)

@st.cache
def knn_accuracies():
    y = [train_knn(i) for i in range(1,21)]
    return y
