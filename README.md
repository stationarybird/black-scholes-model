Options Pricing Models

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-7bss584ezla.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### Inputs

Can first select between either Black-Scholes or Binomial Option Pricing Models

1. Ticker. Takes input and puts into Yahoo API

2. Strike Price. Price at which option can be exercised

3. Risk Free Rate. 

4. Volatility.

5. Exercise Date. 

### Output

Click either button to find either call or put option price given your inputs. 

### Future Developments

Add stock graphs, adjustable time for the graphs, and work on Binomial Option Model and Monte Carlo Simulation
