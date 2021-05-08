import os
import time
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

from ML_models import train_svm,train_knn,knn_accuracies,train_log_regression,log_regression_stats





###################### Settings ######################
root_path = os.path.dirname(os.path.realpath(__file__))
#######################################################


# Dataset
st.write('# Amazon Analysis')
st.write('---')
st.write('# 1. Dataset : ')

st.write("This Dataset was Scrapped From [Amazon's](https://www.amazon.fr/) website and cleaned")
dataset_path = os.path.join(root_path, '..', 'common', 'reviews_dataset.csv')
chart_data = pd.read_csv(dataset_path)
#st.write(chart_data)
#################

##################################################
# Models :
##################################################

# SVM :
##################################################
st.write('# 2. ML-Models ')
st.write('## 2.1 SVM (Support Vector Machines) : ')
st.write(' Choose your parameters to train the **SVM** model : ')

def format_func(option):
    return svm_decision_options[option]

if st.checkbox('Show Parameters :'):
    col1, col2 = st.beta_columns(2)
    # Row
    svm_kernel = col1.selectbox('Kernel', ['rbf','linear','poly','sigmoid'])
    svm_degree = col2.slider('Degree', min_value=2, max_value=5)

    # Row
    svm_c = col1.number_input('C',min_value=0.0,value= 1.0)
    svm_gamma = col2.number_input('Gamma', min_value=0.0, value=1e-2)

    # Row
    svm_decision_options = {'ovo' : 'ovo (One vs One)' ,'ovr': 'ovr (One vs Rest)' }

    svm_decision = st.selectbox('Decision Function Shape', options = list(svm_decision_options.keys()), format_func= format_func)

    # Row
    svm_btn = st.button('[SVM] Submit')

    if svm_btn :
        st.spinner()
        with st.spinner(text='In progress'):
            svm_acc = train_svm(svm_kernel, svm_degree, svm_c, svm_gamma, svm_decision)
            time.sleep(5)
            st.success(f'Accuracy : {svm_acc}')


# Row
st.write('## Best Parameters (via **GridSearchCv**): ')
if st.checkbox('Show Best Parameters :'):
    best_params = st.json({'kernel':'rbf','C':'1000','Gamma':'0.001'})
##################################################



# KNN :
##################################################
st.write('## 2.2 KNN ($k$-nearest neighbors) : ')
st.write(' Choose your parameters to train the **KNN** model : ')

if st.checkbox('Show Parameters : '):
    col1, col2 = st.beta_columns(2)
    # Row
    knn_neigh = col1.number_input('n_neighbors', min_value=1, max_value=20)
    knn_weigh = col2.selectbox('weights', ['uniform','distance'])

    # Row
    knn_metric = st.selectbox('metric', ['minkowski','euclidean','manhattan','cosine'])


    # Row
    knn_btn = st.button('[KNN] Submit ')

    if knn_btn:
        st.spinner()
        with st.spinner(text='In progress'):
            knn_acc = train_knn(knn_neigh, knn_weigh, knn_metric)
            time.sleep(5)
            st.success(f'Accuracy : {knn_acc}')

if st.checkbox('Show Accuaracy Stats :'):
    x = list(range(1,21))
    y = knn_accuracies()

    knn_acc_df = pd.DataFrame({'Number Of Neighbors':x,'Accuracy':y},columns=['Number Of Neighbors', 'Accuracy'])


    knn_acc_chart = alt.Chart(knn_acc_df).mark_line().encode(
      x=alt.X('Number Of Neighbors:N'),
      y=alt.Y('Accuracy:Q'),
    ).properties(title="Knn Accuaracies in function of n_neighbors")
    st.altair_chart(knn_acc_chart, use_container_width=True)


# Row
st.write('## Best Parameters (via **GridSearchCv**): ')
if st.checkbox('Show Best Parameters : '):
    best_params = st.json({'n_neighbors':5,'weights':'uniform','metric':'Manhattan'})
##################################################


# Logistic Regression :
##################################################
st.write('## 2.3 Logistic Regression : ')
st.write(' Choose your parameters to train the **Log_Reg** model : ')

if st.checkbox('Show Parameters :  '):
    col1, col2 = st.beta_columns(2)

    # Row
    log_c = col1.number_input('C ',min_value=0.0,value= 1.0)
    log_penalty = col2.selectbox('penalty', ['l1','l2','elasticnet','none'])

    # Row
    log_tol = col1.number_input('tol', min_value=0.0, value=1e-4)
    log_solver = col2.selectbox('solver', ['newton-cg','lbfgs','liblinear','sag','saga'])


    # Row
    log_btn = st.button('[LogReg] Submit')

    if log_btn :
        st.spinner()
        with st.spinner(text='In progress'):
            log_acc = train_log_regression(log_c, log_penalty, log_tol, log_solver)
            time.sleep(5)
            st.success(f'Accuracy : {log_acc}')

if st.checkbox('Show Logistic Regression Stats : '):
    x , y_1 , y_2= log_regression_stats()

    log_acc_df = pd.DataFrame({'C':x,'None':y_1,'L2':y_2},columns=['C', 'None','L2'])

    log_acc_df = log_acc_df.melt('C', var_name='name', value_name='Accuracy')

    log_acc_chart = alt.Chart(log_acc_df).mark_line().encode(
      x=alt.X('C:N'),
      y=alt.Y('Accuracy:Q'),
      color=alt.Color("name:N")
    ).properties(title="Log-Reg Accuaracies in function of penalty and C")
    st.altair_chart(log_acc_chart, use_container_width=True)



# Row
st.write('## Best Parameters (via **GridSearchCv**): ')
if st.checkbox('Show Best Parameters :  '):
    best_params = st.json({'penalty':'l2','C':'1000','solver':'lbfgs'})
##################################################








