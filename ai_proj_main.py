import streamlit as st
import pandas as pd
import pickle
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\fake.pkl', 'rb') as f:
    x=pickle.load(f)
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\sarc.pkl','rb') as g:
    y=pickle.load(g)
url=input()
print(x.predict(url))
