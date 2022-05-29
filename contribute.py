import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import joblib

st.header("Contribute to our dataset")
a = st.number_input("Enter the Id of Car",1,800)
b = st.number_input("Enter the symboling of car", -1,4)
c = st.text_input("Enter the name of car")
d = st.text_input("Enter fuel type of car")
e = st.text_input("Enter aspiration of car from turbo and std")
f= st.text_input("Enter doornumber of car from two and four" )
g = st.text_input("Enter type of carbody like convertible, hatchback, wagon, sedan etc")
pq=st.text_input("Enter Engine Location")
mn=st.text_input("Enter Drive wheel")
h = st.number_input("Enter wheel base ",80,150)
i = st.number_input("Enter Car Length", 80,200)
j = st.number_input("Enter Car Widht", 80,200)
k = st.number_input("Enter Car height", 200,1000)
ab = st.number_input("Enter Car Weight", 200,1000)
cd = st.text_input("Enter engine type like dohc")
l = st.text_input("Enter Cylinder Number")
m = st.number_input("Enter Car Engine Size", 80,200)
n = st.text_input("Enter Fuel System mpfi or lpj")
o = st.number_input("Enter bore ratio", 1.00,20.00)
p = st.number_input("Enter stroke ", 1.00,20.00)
q = st.number_input("Enter compression ratio", 1.00,20.00)
r = st.number_input("Enter horsepower", 100,500)
s = st.number_input("Enter peakrpm", 500, 5000)
t = st.number_input("Enter citympg", 20,100)
u = st.number_input("Enter highwaympg", 20,100)
v = st.number_input("Enter price", 500000,2000000)
if st.button("Submit"):
    to_add = {"car_ID":a , "symboling":b,	"CarName":c ,"fueltype":d,	"aspiration":e,	"doornumber":f,	"carbody":g	, "drivewheel":mn,"enginelocation":pq,
              "wheelbase":h, "carlength":i,"carwidth":j, "carheight":k,	"curbweight":ab,	"enginetype":cd,	"cylindernumber":l,	"enginesize":m,	"fuelsystem":n,
              "boreratio":o, "stroke":p, "compressionratio":q,"horsepower":r,"peakrpm":s, "citympg":t, "highwaympg":u, "price":v}
    to_add=pd.DataFrame({k: [v] for k, v in to_add.items()})
    to_add.to_csv("contri.csv", mode='w+', header=False, index=False)
    st.success("Submitted")




