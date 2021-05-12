import streamlit as st
import streamlit.components.v1 as components
from view.html_variables import buy_a_coffee
from utils.dna_edition import UtilsDNA

st.title('DNA codons conversion')
st.image('./images/dna.png')
old_codon = st.text_input('codon to change', value="ATC", max_chars=3, help="The codon you wish to subsitute")
new_codon = st.text_input("codon's new value", value="TAG", max_chars=3, help="The new value of the codon you substituted")

dna = st.text_area('the input dna')
if dna:
    if UtilsDNA.check_divided_by_three(dna):
        st.write('Number of letters can be divided by three')
        if st.button("Generate new dna"):
            new_dna = UtilsDNA.change_condon_from_adn_string(
                                                         adn_string=dna,
                                                         codon_to_change=old_codon,
                                                         new_codon_value=new_codon
                                                         )
            st.write(new_dna)

    else:
        st.write('The number of letter of your string is not divided by three')





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