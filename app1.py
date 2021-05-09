import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# STOCK PRICE TRACKER 
""")

st.write("""
## NASDAQ 
""")

#define the ticker symbol
tickerSymbol = 'COMP'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2011-4-30', end='2021-4-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
### NASDAQ Closing Prices
""")
st.line_chart(tickerDf.Close)

st.write("""
### NASDAQ Volume Prices
""")
st.line_chart(tickerDf.Volume)

st.write("""
## AMD 
""")

tickerSymbol = 'AMD'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-4-30', end='2021-4-30')

st.write("""
### AMD Closing Prices
""")
st.line_chart(tickerDf.Close)
st.write("""
### AMD Volume Prices
""")
st.line_chart(tickerDf.Volume)

st.write("""
## TESLA
""")
tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-4-30', end='2021-4-30')

st.write("""
### TESLA Closing Prices
""")
st.line_chart(tickerDf.Close)
st.write("""
### TESLA Volume Prices
""")
st.line_chart(tickerDf.Volume)