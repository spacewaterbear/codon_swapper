
"""
credits : https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030

"""

import streamlit as st

import streamlit.components.v1 as components
from view.html_variables import buy_a_coffee
# Custom imports
from pages import codon_conversion, restriction_site_extraction

# Create an instance of the app

st.set_page_config(page_title="DNA App", page_icon="🍵", layout="wide")
# Title of the main page
st.title("DNA App")


page_mapping = {
    "Codon Conversion": codon_conversion.codon_app,
    "Restriction Site Extraction": restriction_site_extraction.restriction_app
}

app_to_display = st.sidebar.selectbox("Please Choose an Application", options=list(page_mapping.keys()), index=1)

page_mapping[app_to_display]()


st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")
st.write("   \n")

st.markdown("***")
st.write("Made with ❤️ by 🍌")

components.html(buy_a_coffee)