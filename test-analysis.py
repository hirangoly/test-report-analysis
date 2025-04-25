import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🧪 Test Report Dashboard")

uploaded_file = st.file_uploader("📤 Upload your Test Report (CSV format)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Test Report")
    st.dataframe(df, use_container_width=True)

    if 'Result' in df.columns:
        st.subheader("📊 Test Result Summary")
        result_counts = df['Result'].value_counts()
        st.bar_chart(result_counts)

        pass_rate = (result_counts.get('Pass', 0) / result_counts.sum()) * 100
        st.metric(label="✅ Pass Rate", value=f"{pass_rate:.2f}%")

        st.subheader("❌ Failed Test Cases")
        failed_tests = df[df['Result'] == 'Fail']
        st.dataframe(failed_tests, use_container_width=True)

        st.subheader("📅 Test Case Distribution Over Time")
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            time_df = df.groupby([df['Date'].dt.date, 'Result']).size().unstack(fill_value=0)
            st.line_chart(time_df)

        st.subheader("🔍 Filter Tests by Module")
        if 'Module' in df.columns:
            selected_module = st.selectbox("Select Module", df['Module'].unique())
            st.dataframe(df[df['Module'] == selected_module], use_container_width=True)
    else:
        st.warning("Column 'Result' not found in uploaded file. Please include it to enable result analysis.")
else:
    st.info("Upload a CSV file containing test report with columns like 'Result', 'Module', and 'Date'.")
