import streamlit as st
import pandas as pd
import numpy as np
import sys
import traceback

# Configure page - must be first Streamlit command
st.set_page_config(
    page_title="NYC Taxi Analytics", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("NYC Taxi Analytics Dashboard")
st.write("Welcome to NYC Taxi Analytics Dashboard powered by Databricks")

# Add error handling wrapper
try:
    # Sample data
    @st.cache_data
    def get_data():
        dates = pd.date_range('2016-01-01', periods=1000, freq='H')
        data = {
            'datetime': dates,
            'distance': np.random.exponential(2.5, 1000),
            'fare': np.random.exponential(12, 1000)
        }
        return pd.DataFrame(data)

    df = get_data()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Trips", f"{len(df):,}")
    with col2:
        st.metric("Avg Fare", f"${df['fare'].mean():.2f}")
    with col3:
        st.metric("Avg Distance", f"{df['distance'].mean():.2f} mi")

    st.subheader("Sample Data")
    st.dataframe(df.head(10))

    st.success("Dashboard loaded successfully!")
    
except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
    st.code(traceback.format_exc())
    sys.exit(0)  # Don't crash, just exit gracefully
