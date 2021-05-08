import os
import pandas as pd
import streamlit as st

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

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
def train_svm(C,kernel,degree=2,gamma=1e-3,decision_function='ovo'):
    X_train, X_test, y_train, y_test = load_data()
    svm = SVC(kernel=kernel,degree=degree, C=C,gamma=gamma, decision_function_shape=decision_function)
    svm.fit(X_train, y_train)
    return svm.score(X_test,y_test)

@st.cache
def svm_stats():
    c_ = [1e-4,1e-3,1e-2,1e-1,1,2,3,5,10,20,30,50,100,200,500,1000,2000,5000,10000]
    rbf = [train_svm(c,kernel='rbf') for c in c_]
    linear = [train_svm(c,kernel='linear') for c in c_]
    return c_,rbf,linear


@st.cache
def train_knn(n_neighbors,weights='uniform',metric='minkowski'):
    X_train, X_test, y_train, y_test = load_data()
    knn = KNeighborsClassifier(n_neighbors=n_neighbors,weights=weights, metric=metric)
    knn.fit(X_train, y_train)
    return knn.score(X_test,y_test)

@st.cache
def knn_accuracies():
    return [train_knn(i) for i in range(1,21)]


@st.cache
def train_log_regression(C,penalty='l2',tol=1e-4,solver='lbfgs'):
    X_train, X_test, y_train, y_test = load_data()
    log_reg = LogisticRegression(C=C,penalty=penalty,tol=tol,solver=solver)
    log_reg.fit(X_train, y_train)
    return log_reg.score(X_test,y_test)

@st.cache
def log_regression_stats():
    c_ = [1e-4,1e-3,1e-2,1e-1,1,2,3,5,10,20,30,50,100,200,500,1000,2000,5000,10000]
    l1_ = [train_log_regression(c,penalty='none') for c in c_]
    l2_ = [train_log_regression(c,penalty='l2') for c in c_]
    return c_,l1_,l2_


