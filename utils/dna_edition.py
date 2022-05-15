import re
from typing import List


class UtilsDNA:
    @staticmethod
    def clean_string(string):
        return string.strip().upper()

    @staticmethod
    def check_divided_by_three(string: str):
        string = UtilsDNA.clean_string(string)
        if len(string)%3 == 0:
            return True
        else:
            return False

    @staticmethod
    def split_string_by_n_characters(string: str, n=3):
        string = UtilsDNA.clean_string(string)
        assert len(string)%n == 0, "Length of adn is not divided by the divider"
        return [string[i:i+3] for i in range(0, len(string), 3)]

    @staticmethod
    def change_codon_by_another_one(dna_list, old_codon_value, new_codon_value):
        dna_list_edited = [codon if codon != old_codon_value else new_codon_value for codon in dna_list]
        return dna_list_edited

    @staticmethod
    def change_condon_from_adn_string(adn_string, codon_to_change, new_codon_value):
        dna_list = UtilsDNA.split_string_by_n_characters(string=adn_string)
        dna_list_edited = UtilsDNA.change_codon_by_another_one(dna_list, old_codon_value=codon_to_change, new_codon_value=new_codon_value)
        dna_string_edited = "".join(dna_list_edited).upper()
        return dna_string_edited

    @staticmethod
    def check_if_seq_is_belonging_to_dna(dna_sequence: str) -> bool:
        for letter in dna_sequence:
            if letter not in ["A", "C", "G", "T"]:
                return letter

        return True


    @staticmethod
    def extract_dn_between_to_strings(dna_string, start_string, end_string) -> List[str]:
        matches = re.findall(f"{start_string.upper()}([A-Za-z]+){end_string.upper()}", dna_string)
        return matches

    @staticmethod
    def generate_fasta_from_information(sid: str, name: str, nb_match: int, sequence: str) -> str:
        header = f"{sid} {name} / {nb_match}"
        return f">{header}\n{sequence}\n"