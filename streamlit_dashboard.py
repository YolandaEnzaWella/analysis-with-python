import streamlit as st
import pandas as pd
import altair as alt

# Load your dataset
df = pd.read_csv("/Users/Yola/Analisis_dengan_Python/PRSA_Data_Aotizhongxin_20130301-20170228.csv")

# Title for your Streamlit app
st.title("Air Quality Dashboard")

# Display the first few rows of the dataset
st.subheader("Data Overview")
st.write(df.head())

# Data Cleaning: Remove rows with missing values
df.dropna(inplace=True)

# Data overview function
def data_overview(df):
    st.subheader("Overview of the Dataset")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write("Number of columns: ", df.shape[1])
    st.write("Features: ", df.columns.tolist())
    st.write("Missing Values: ", df.isna().sum().values.sum())
    st.write("Unique values: ", df.nunique())

data_overview(df)

# Explore the most common value for each pollutant
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
most_common_pollutants = {}
for pollutant in pollutants:
    most_common_pollutant = df[pollutant].mode().values[0]
    most_common_pollutants[pollutant] = most_common_pollutant

st.subheader("Most Common Pollutants")
for pollutant, value in most_common_pollutants.items():
    st.write(f"{pollutant}: {value}")

# Visualization - Daily and Monthly Data
st.subheader("Daily and Monthly Data Visualization")

# Convert 'year', 'month', and 'day' to a datetime column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# Aggregating data for daily and monthly averages
daily_data = df.groupby('date').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})
monthly_data = df.groupby('month').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})

# Create line charts for daily and monthly data
st.subheader("Daily Data")
st.line_chart(daily_data)

st.subheader("Monthly Data")
st.line_chart(monthly_data)

# You can add more charts and analysis as needed
