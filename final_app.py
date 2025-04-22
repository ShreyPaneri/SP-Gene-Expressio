
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="SP Gene Expressio", layout="wide")

st.title("🧬 SP Gene Expressio - Breast Cancer Explorer")

@st.cache_data
def load_data():
    df = pd.read_csv("final_data.csv")
    return df

data = load_data()

gene_options = sorted(data['Gene'].unique())
selected_gene = st.selectbox("Select a Gene:", gene_options)

filtered_data = data[data['Gene'] == selected_gene]

st.write(f"### Expression Levels for {selected_gene}")
fig = px.box(filtered_data, x="SampleType", y="Expression", points="all", color="SampleType",
             labels={"Expression": "Expression Level", "SampleType": "Sample Type"})
st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_data)
