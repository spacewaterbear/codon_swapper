import streamlit as st
from utils.dna_edition import UtilsDNA

st.title('DNA condon conversion')
st.image('./images/dna.png')
old_codon = st.text_input('condon to change', value="ATC", max_chars=3, help="The codon you wish to subsitute")
new_codon = st.text_input("condon's new value", value="TAG", max_chars=3, help="The new value of the codon you substituted")

dna = st.text_area('the input dna')
if dna:
    if UtilsDNA.check_divided_by_three(dna):
        if st.button("Generate new dna"):
            new_dna = UtilsDNA.change_condon_from_adn_string(
                                                         adn_string=dna,
                                                         codon_to_change=old_codon,
                                                         new_codon_value=new_codon
                                                         )
            st.write(new_dna)

    else:
        st.write('The number of letter of your string is not divided by three')