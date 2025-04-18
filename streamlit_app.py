import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SP Gene Expressio", layout="wide")

st.title("SP Gene Expressio: Gene Expression Explorer")

uploaded_file = st.file_uploader("Upload your gene expression CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    gene_column = st.selectbox("Select gene name column", df.columns)
    value_column = st.selectbox("Select expression value column", df.columns)
    group_column = st.selectbox("Select sample/tissue/group column (optional)", df.columns)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head(10))

    st.subheader("Gene Expression Plot")

    if group_column:
        fig = px.box(df, x=group_column, y=value_column, points="all", color=group_column,
                     title=f"Expression of {gene_column} grouped by {group_column}")
    else:
        fig = px.histogram(df, x=value_column, nbins=30,
                           title=f"Distribution of Expression Values for {gene_column}")

    st.plotly_chart(fig, use_container_width=True)
