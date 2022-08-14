# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:25:40 2022

@author: Sony
"""

import pickle
import json
import numpy as np
import streamlit as st

model=pickle.load(open('model1.pkl','rb'))
with open("columns.json", "r") as f:
     data_columns = json.load(f)['data_columns']
     locations = data_columns[3:] 

def predicted_price(location,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(model.predict([x])[0],2)


if __name__ == '__main__':
    st.title("Bangalore House Price Prediction")
    
    st.subheader('Please enter the required details:')
    sqft=st.text_input('Square  Feet')
    bhk=st.radio('BHK',[1,2,3,4,5],horizontal=True)
    bath=st.radio('BATHROOM',[1,2,3,4,5],horizontal=True)
    location=st.selectbox('Locations', locations)
    result=st.button('House Price in Lakhs')
   
    if result:
        real_price=predicted_price(location,sqft,bath,bhk)
        st.success(real_price)
    
  
     
     