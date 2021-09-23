# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:54:40 2021

@author: ysun

code from https://www.youtube.com/watch?v=JwSS70SZdyM
freeCodeCamp.org
https://github.com/dataprofessor/streamlit_freecodecamp/tree/main/app_1_simple_stock_price
"""

import yfinance as yf
import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

def strdate(date):
    yr=str(date.year)
    mt=str(date.month)
    d=str(date.day)
    return yr+'-'+mt+'-'+d

st.write("""
# Simple Glencore Stock Price App

Shown are the stock **closing price** and ***volume*** of Glencore in the past five years

""")

#Markdown cheatsheet for fonts

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GLNCY'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
today = date.today()
startdate = today - relativedelta(years=5)

todaystring = strdate(today)
startstring = strdate(startdate)
tickerDf = tickerData.history(period='1d', start=startstring, end=todaystring)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
         Closing Price
         """)
st.line_chart(tickerDf.Close)
st.write("""
         Volume
         """)
st.line_chart(tickerDf.Volume)
