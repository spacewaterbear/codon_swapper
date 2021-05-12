
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