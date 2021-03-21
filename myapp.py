import yfinance as yf
import streamlit as st
import pandas as pd


st.write(
    """
    # Simple Stock Price App

    Shown are the stock **closing price** and ***volume*** of Google!
    """
)

# Define the ticker symbol
tickerSymbol = "GOOGL"

# Get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2011-2-21", end="2021-2-21")
# Open High Low Close Volume Dividends Stock Splits

st.write(
    """
    ## Closing Price
    """
)
st.line_chart(tickerDf.Close)
st.write(
    """
    ## Volume Price
    """
)
st.line_chart(tickerDf.Volume)
