
import streamlit as st
from io import StringIO
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)

data=pd.read_excel(uploaded_file,header=3)

a=data.groupby(['OLT IP','Original UpTime(%)'])
df1=data[['OLT IP','Original UpTime(%)']]

OLT_average=df1.groupby(['OLT IP']).mean()

new=pd.merge(data,OLT_average,on='OLT IP',how='inner')

new.rename(columns={'Original UpTime(%)_y':'OLT Average'},inplace=True)


def highlight(x):
    return ['background-color: red' if v<70 else '' for v in new['UpTime(%)']]
    


b=new.style.apply(highlight)
st.write(new)
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv=convert_df(new)
st.download_button("Download",data=csv,on_click='test.csv',mime='text/csv')

