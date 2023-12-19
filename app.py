import streamlit as st
import pandas as pd
import pickle


df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title("Laptop Price Predictor")

Company = st.selectbox("Brand",sorted(df['Company'].unique()))
TypeName = st.selectbox("Laptop Type",sorted(df['TypeName'].unique()))
Ram = st.selectbox("Ram(in GBs)",[2,4,6,8,12,16,24,32,64])
Weight = st.selectbox('Weight of the Laptop',sorted(df['Weight'].unique()))
os = st.selectbox("OS",sorted(df['OS'].unique()))
GpuBrand = st.selectbox("GPU",sorted(df['Gpu Brand'].unique()))
TouchScreen = st.selectbox("TouchScreen",['Yes','No'])
Ips = st.selectbox("IPS Display",['Yes','No'])
HDD = st.selectbox("Hard Drive",[0,128,256,512,1024,2048])
SSD = st.selectbox("SSD size(in GBS)",[0,8,128,256,512,1024])
CpuBrand = st.selectbox("Processor",sorted(df['Cpu Brand'].unique()))
screensize = st.text_input("Screen Size")
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

if st.button("Predict Price"):
    if TouchScreen == 'Yes':
        TouchScreen = 1
    else:
        TouchScreen = 0

    if Ips == 'Yes':
        Ips = 1
    else:
        Ips = 0

    TouchScreen = int(TouchScreen)
    screensize = int(screensize)
    x = resolution.split('x')[0]
    x = int(x)
    y = resolution.split('x')[1]
    y = int(y)
    ppi = ((x**2 + y**2)**0.5)/screensize
    ppi = float(ppi)

    result = pipe.predict(pd.DataFrame({
        'Company': [Company],
        'TypeName': [TypeName],
        'Ram': [Ram],
        'Weight': [Weight],
        'TouchScreen': [TouchScreen],
        'Ips': [Ips],
        'ppi': [ppi],
        'Cpu Brand': [CpuBrand],
        'HDD': [HDD],
        'SSD': [SSD],
        'Gpu Brand': [GpuBrand],
        'OS': [os]
    }))

    result = result[0]
    st.title(str(int(result))+"Rs")
