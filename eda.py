#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 00:05:20 2021

@author: shailesh
"""


import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from PIL import Image
import os

st.title('Food Demand Forecasting')
our_image = Image.open(os.path.join('food.png'))
st.image(our_image)

@st.cache
def load_data(nrows):
    data = pd.read_csv("train.csv",nrows=nrows)
    return data

@st.cache
def load_center_data(nrows):
    data = pd.read_csv("fulfilment_center_info.csv",nrows=nrows)
    return data

@st.cache
def load_meal_data(nrows):
    data = pd.read_csv("meal_info.csv",nrows=nrows)
    return data

weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

#Weekly Demand Data

st.subheader("Weekly Demand Data")
st.write(weekly_data)
st.bar_chart(weekly_data['num_orders'])
df = pd.DataFrame(weekly_data[:200],columns = ['num_orders','checkout_price','base_price'])
df.hist()


st.line_chart(df)

st.subheader("Number of Orders vs Base Price")
chart_data = pd.DataFrame(weekly_data[:40],columns = ['num_orders','base_price'])
st.area_chart(chart_data)

#center information

st.subheader('Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information Data')
    st.write(center_info_data)

st.subheader("Number of Orders vs Base Price")
    
st.bar_chart(center_info_data['region_code'])
st.bar_chart(center_info_data['center_type'])

hist_data = [center_info_data['center_id'],center_info_data['region_code']]
group_labels = ['Centre Id','Region Code']
fig = ff.create_distplot(hist_data,group_labels,bin_size=[10,25])
st.plotly_chart(fig,use_container_width = True )

st.subheader('Meal Information')
st.write(meal_data)
st.bar_chart(meal_data['cuisine'])
agree = st.button('Click to see Categories of Meals')
if agree:
    st.bar_chart(meal_data['category'])
    




    
