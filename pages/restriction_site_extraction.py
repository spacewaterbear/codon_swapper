from loguru import logger
from Bio import SeqIO

import streamlit as st

from utils.dna_edition import UtilsDNA


def restriction_app():
    st.title('Extract restriction sites')
    st.write("This application use the python Bio library. Please check out the documentation for more information. : https://www.bioinfo.help/")
    st.write("""
    This application is made for the extraction of restriction sites from DNA sequences.
    1. put the restriction enzyme site in the input box
    2. load your .ab1 file. The script will extract the restriction sites and all you to download your fasta file.
    """)
    left_col, right_col = st.columns(2)
    with left_col:
        left_restriction_site = st.text_input('Left restriction site', value='ATC')
        is_valid = UtilsDNA.check_if_seq_is_belonging_to_dna(left_restriction_site)
        if isinstance(is_valid, str):
            st.warning(f'Letter {is_valid} is not in the dna')
    with right_col:
        right_restriction_site = st.text_input('Right restriction site', value='GAT')
        is_valid = UtilsDNA.check_if_seq_is_belonging_to_dna(right_restriction_site)
        if isinstance(is_valid, str):
            st.warning(f'Letter {is_valid} is not in the dna')

    up_files = st.file_uploader('Upload your file', accept_multiple_files=True)
    logger.debug(f"Uploaded files: {type(up_files)}")
    final_fasta = ""
    if up_files:
        all_matchs = []
        for file in up_files:
            for record in SeqIO.parse(file, "abi"):
                st.write(f"{file.name}, id {(record.id)}")
                st.write(record.seq)
                matches = UtilsDNA.extract_dn_between_to_strings(str(record.seq), left_restriction_site, right_restriction_site)
                if matches:
                    matches_str = '\n'.join(matches)
                    st.write(f"{len(matches)} matches : {matches_str}")
                    all_matchs += matches
                    sub_part_fasta = ""
                    for i, match in enumerate(matches):
                        sub_part_fasta += UtilsDNA.generate_fasta_from_information(sid=record.id, name=record.name, nb_match=i+1, sequence=match)
                    final_fasta += sub_part_fasta
                else:
                    st.warning(f"No match found for {file.name}")


    st.download_button('Download your file', final_fasta, file_name='output.fasta')