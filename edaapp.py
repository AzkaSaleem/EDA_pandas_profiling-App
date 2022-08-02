import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport, profile_report
from streamlit_pandas_profiling import st_profile_report

#web app title
st.markdown('''
# ** Streamlit EDA App **.
### You can select the data you want to explore and see the results in the sidebar.
''')

# how to upload file from pc
with st.sidebar.header("Upload Data"):
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv", "txt"])
    df= sns.load_dataset("iris")
    st.sidebar.markdown("[Example csv file](https://github.com/dataprofessor/data/blob/master/delaney.csv)")

#profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv= pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df,explorative=True)
    st.header("Input df")
    st.write(df)
    st.write("---")
    st.header("Profiling Report with pandas_profiling")
    st_profile_report(pr)
else:
    st.info("You haven't uploaded any file.")
    if st.button("press to use example data"):

        def load_data():
            a= pd.DataFrame(np.random.rand(10,5),
                            columns=['a','b','c','d','e'])  
            return a
        df = load_data()
        pr = ProfileReport(df,explorative=True)
        st.header("Input df")
        st.write(df)
        st.write("---")
        st.header("Profiling Report with pandas_profiling")
        st_profile_report(pr)