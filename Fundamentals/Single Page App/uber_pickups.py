import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# 🚖 UBER PICKUPS DEMO APP
# -----------------------------
st.title("🚖 Uber Pickups in NYC")

# Constants
DATE_COLUMN = 'date/time'
DATA_URL = (
    'https://s3-us-west-2.amazonaws.com/'
    'streamlit-demo-data/uber-raw-data-sep14.csv.gz'
)

# -----------------------------
# 🔄 Data Loading (with caching)
# -----------------------------
@st.cache_data
def load_data(nrows):
    """Loads and preprocesses Uber data"""
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # Convert all column names to lowercase
    data.rename(str.lower, axis='columns', inplace=True)
    # Convert date/time column to datetime object
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Display loading status
with st.spinner("Loading data..."):
    data = load_data(10000)
st.success("✅ Data loaded successfully (with caching)")

# -----------------------------
# 📦 Raw Data Display
# -----------------------------
if st.checkbox("Show raw data"):
    st.subheader("📋 Raw Data (first 10,000 rows)")
    st.write(data)

# -----------------------------
# 📊 Histogram of Pickups by Hour
# -----------------------------
st.subheader("📈 Number of Pickups by Hour")

# Get histogram values
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# -----------------------------
# 🕒 Hour Slider & Pickup Map
# -----------------------------
st.subheader("🗺️ Map of Pickups at Selected Hour")

# Select hour
hour_to_filter = st.slider("Select hour of the day", 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# Display filtered data on map
st.map(filtered_data)
