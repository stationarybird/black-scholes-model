import streamlit as st
import yfinance as yf
import math
from scipy.stats import norm
from datetime import date

st.title("Black Scholes Model")
    
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

        d1 = (math.log(s/k)+(r+0.5*vol**2)*t)/(vol*math.sqrt(t))
        d2 = d1 - vol*math.sqrt(t)

        call = st.form_submit_button(label = "Calculate Call Price")
        put = st.form_submit_button(label = "Calculate Put Price")
        if call:
            c = s * norm.cdf(d1) - k*math.exp(-r*t)*norm.cdf(d2)
            st.write("Call option price: $", round(c, 2))
        if put:
            p = k * math.exp(-r*t) * norm.cdf(-d2) - s*norm.cdf(-d1)
            st.write("Put option price: $", round(p, 2))
    else:

        call = st.form_submit_button(label = "Calculate Call Price")
        put = st.form_submit_button(label = "Calculate Put Price")
        




        




