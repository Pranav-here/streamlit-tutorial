import streamlit as st
import pandas as pd
import numpy as np
import time

# --- HEADER SECTION ---
st.title("🎯 Streamlit Demo: Core Concepts")
st.markdown("This app demonstrates various Streamlit widgets and features with annotated examples.")

# --- DATA DISPLAY SECTION ---
st.header("📊 Working with DataFrames")

# Static DataFrame
st.subheader("1. Static DataFrame")
sample_df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write(sample_df)

# Dynamic Random DataFrame
st.subheader("2. Styled DataFrame")
styled_df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f"Col {i+1}" for i in range(20)]
)
st.dataframe(styled_df.style.highlight_max(axis=0))

# Table (non-scrollable, fixed-size)
st.subheader("3. Static Table")
st.table(styled_df.head().style.highlight_max(axis=0))  # Just show first 5 rows for clarity

# --- VISUALIZATION SECTION ---
st.header("📈 Visualizations")

# Line Chart
st.subheader("4. Line Chart")
line_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(line_data)

# Map Visualization
st.subheader("5. Map")
map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],  # SF coordinates
    columns=['lat', 'lon']
)
st.map(map_df)

# --- INTERACTIVITY SECTION ---
st.header("🧠 Widgets & User Inputs")

# Slider
st.subheader("6. Slider Input")
val = st.slider("Pick a value for x")
st.write(f"x² = {val ** 2}")

# Text Input
st.subheader("7. Text Input")
user_name = st.text_input("Enter your name")
if user_name:
    st.write(f"Hello, {user_name}!")

# Checkbox
st.subheader("8. Conditional Display with Checkbox")
if st.checkbox("Show a random DataFrame"):
    st.dataframe(pd.DataFrame(np.random.randn(10, 3), columns=["X", "Y", "Z"]))

# Selectbox
st.subheader("9. Selectbox")
fav_number = st.selectbox("Choose your favorite number", sample_df['Column 1'])
st.write(f"You selected: {fav_number}")

# Sidebar Inputs
st.sidebar.header("📌 Sidebar Controls")
contact_method = st.sidebar.selectbox("Preferred Contact Method", ("Email", "Phone", "Mobile"))
range_slider = st.sidebar.slider("Select a value range", 0.0, 100.0, (25.0, 75.0))

# Columns
st.subheader("10. Columns and Radio Buttons")
col1, col2 = st.columns(2)
with col1:
    st.button("Click me!")

with col2:
    house = st.radio("Choose your house:", ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"])
    st.write(f"You're in **{house}**!")

# --- PROGRESS BAR EXAMPLE ---
st.subheader("11. Progress Bar")
progress_text = st.empty()
progress_bar = st.progress(0)

for i in range(5):
    progress_text.text(f"Processing {i+1}/5...")
    progress_bar.progress((i+1) * 20)
    time.sleep(1)

# --- ADVANCED CONCEPTS SECTION ---
st.header("🧠 Advanced Streamlit Concepts")

# Caching for expensive computations
st.subheader("12. Caching")
@st.cache_data
def load_heavy_data():
    time.sleep(2)  # simulate delay
    return pd.DataFrame(np.random.randn(100, 3))

if st.button("Load cached data"):
    st.write(load_heavy_data())

# Session State
st.subheader("13. Session State Counter")
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if st.button("Increment Counter"):
    st.session_state.clicks += 1
st.write(f"Button clicked {st.session_state.clicks} times.")

# Session DataFrame and color picker
if "scatter_df" not in st.session_state:
    st.session_state.scatter_df = pd.DataFrame(np.random.randn(50, 2), columns=["x", "y"])

st.subheader("14. Dynamic Chart with Color Picker")
picked_color = st.color_picker("Pick a highlight color", "#00f900")
st.scatter_chart(st.session_state.scatter_df, x="x", y="y", color=picked_color)

# --- PLACEHOLDER FOR DATABASE CONNECTION ---
st.subheader("15. Database Connection Example (Commented)")
# Uncomment and configure this if needed
# conn = st.connection("your_db_connection")
# result_df = conn.query("SELECT * FROM your_table")
# st.dataframe(result_df)

# --- PLACEHOLDER FOR MULTI-PAGE NAVIGATION ---
st.header("📄 Page Navigation (Conceptual)")
st.markdown("_To use multipage apps, create separate `.py` files and add them to `.streamlit/pages/` folder._")

# --- STATIC FILE EXAMPLE ---
st.subheader("📁 Static File Display")
st.image("static/cat.png", caption="Static Asset: Cat Image")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | [YourName/Project](https://github.com)")
