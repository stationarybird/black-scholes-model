import streamlit as st
import yfinance as yf
import math
from scipy.stats import norm
from datetime import date

st.title("Finance Models")
    
st.page_link("/pages/blackscholes.py", label="Black Scholes Model", icon="📈")
st.page_link("/pages/binomial.py", label="Binomial Option Model", icon="📈")

        




