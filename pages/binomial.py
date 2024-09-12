import streamlit as st
import yfinance as yf
import math
from scipy.stats import norm
from datetime import date
import numpy as np

st.title("Binomial Option Pricing Model")
    
with st.form("my_form"):

    ticker = st.text_input("Ticker", value="NVDA")

    tick = False
    stock = yf.Ticker(ticker)
    if 'currentPrice' in stock.info:
        s = stock.info['currentPrice']
        tick = True
    else:
        st.error("Invalid ticker symbol or no data available for this ticker. Try again!")

    if tick:
                
        k = st.number_input("Strike Price", value = 0.8*s)

        r = st.slider("Risk Free Rate", 0, 100, format="%d%%", value = 10)

        vol = st.slider("Volatility(σ)", 0, 100, format="%d%%", value = 20)

        r = r/100

        vol = vol/100

        exercisedate = st.date_input("Exercise Date", value = "default_value_today", format = "MM/DD/YYYY")
        today = date.today()
        tdelta = exercisedate - today
        t = (float(tdelta.days)/365.0)
        
        if t == 0:
            st.warning("Exercise date should be in the future. Using a very small value for time to avoid division by zero.")
            t = 1e-10  # Assign a very small positive value to t

        n = 100
        timestep = t/n
        u = math.pow(math.e, vol*math.sqrt(timestep))
        d = 1/u
        p = (math.pow(math.e, r*timestep) - d)/(u - d)

        ST = np.zeros(n+1)
        for j in range(n+1):
            ST[j] = s * (u**j) * (d **(n-j))
        
        call_values = np.maximum(0, ST - k)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                call_values[j] = np.exp(-r *timestep) * (p * call_values[j + 1] + (1 - p) * call_values[j])

        put_values = np.maximum(0, k - ST)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                put_values[j] = np.exp(-r * timestep) * (p * put_values[j + 1] + (1 - p) * put_values[j])

        call = st.form_submit_button(label = "Calculate Call Price")
        put = st.form_submit_button(label = "Calculate Put Price")

        if call:
            c = call_values[0]
            st.write("Call option price: $", round(c, 2))
        if put:
            p = put_values[0]
            st.write("Put option price: $", round(p, 2))
    else:
        call = st.form_submit_button(label = "Calculate Call Price")
        put = st.form_submit_button(label = "Calculate Put Price")
        




        




