#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

def pre_proccess_df(df):
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data one less than the header row
    df.columns = new_header    
    df=df.iloc[:,0:5135] # select the features with high fidelity
    return df

def pre_proccess_labels(labels_df,train=True):
    #Find and drop the index of the molecules with duplicates/same names
    if train is True:        
        index_names = labels_df[(labels_df['mol_number'] == "T1925")|(labels_df['mol_number'] =="T1934")|(labels_df['mol_number'] =="T2801")|(labels_df['mol_number'] =="T7352")].index
        labels_df.drop(index_names, axis=0 ,inplace = True)
        # Remove the "smiles_parent" and"mol_number from dataFrame
        labels_df.drop(["smiles_parent","mol_number"], axis=1,inplace = True)
        labels_df.reset_index(drop=True,inplace = True)               
        labels_df.index = np.arange(1, len(labels_df) + 1)
    else:
        # Remove the "smiles_parent" and"mol_number from dataFrame
        labels_df.drop(["smiles_parent","mol_number"], axis=1,inplace = True)
        labels_df.reset_index(drop=True,inplace = True)               
        labels_df.index = np.arange(1, len(labels_df) + 1)
        
    return labels_df

def pre_proccess_dfassay(assay,X_traindata,train_labels,X_testdata, test_labels):
    #Create a dataset for each assay with its labels
    y_traindata= train_labels[[assay]]
    y_testdata = test_labels[[assay]]
    train=pd.concat([X_traindata,y_traindata],axis=1)
    test=pd.concat([X_testdata,y_testdata],axis=1)
    #Remove moelcules not tested with the assay
    train.dropna(inplace=True)
    test.dropna(inplace=True)
    #Get both train and test data and labels
    y_train=train[assay]
    X_train=train.drop([assay],axis=1)
    y_test=test[assay]
    X_test=test.drop([assay],axis=1)
    
    return X_train, y_train, X_test, y_test



