from utils.dna_edition import UtilsDNA
import pytest


splitted_data = [
    ("ATCGTTATA", ["ATC","GTT","ATA"]),
    (" ATCGTTATA", ["ATC","GTT","ATA"]),
]

def test_split_string_by_n_characters_bad_input():
    n = 3
    string = "ATCGTTATAA"
    error_message = "Length of adn is not divided by the divider"
    with pytest.raises(AssertionError, match=error_message):
                UtilsDNA.split_string_by_n_characters(string)

@pytest.mark.parametrize(("dna_str, dna_list"), splitted_data)
def test_split_string_by_n_characters(dna_str, dna_list):
    assert UtilsDNA.split_string_by_n_characters(dna_str, n=3) == dna_list




codon_conversion = [
    (["ATC", "GTT", "ATA"], "ATC", "TAG", ["TAG", "GTT", "ATA"]),
]
@pytest.mark.parametrize(("dna_list, old_codon_value, new_codon_value, dna_list_edited"), codon_conversion)
def test_change_codon_by_another_one(dna_list, old_codon_value, new_codon_value, dna_list_edited):
    assert UtilsDNA.change_codon_by_another_one(dna_list, old_codon_value, new_codon_value) == dna_list_edited





change_dna_straing = [
    ("ATCGTTATA", "ATC", "TAG", "TAGGTTATA"),
    ("ATCGTTATA ", "ATC", "TAG", "TAGGTTATA"),
]

@pytest.mark.parametrize(("dna_string, old_codon_value, new_codon_value, dna_string_edited"), change_dna_straing)
def test_change_condon_from_adn_string(dna_string, old_codon_value, new_codon_value, dna_string_edited):
    assert UtilsDNA.change_condon_from_adn_string(dna_string, old_codon_value, new_codon_value) == dna_string_edited


is_divided_by_three = [
    ("ATCGTTATA", True),
    ("ATCGTTATAA", False),
]

@pytest.mark.parametrize(("dna_string, boolean"), is_divided_by_three)
def test_is_divided_by_three(dna_string, boolean):
    assert UtilsDNA.check_divided_by_three(dna_string) == boolean


clean_data = [
    ("ATCGTTATA ", "ATCGTTATA"),
    (" ATCGTTATAA", "ATCGTTATAA"),
    (" atcgttata", "ATCGTTATA"),
]

@pytest.mark.parametrize(("dna_string, dna_string_cleaned"), clean_data)
def test_is_divided_by_three(dna_string, dna_string_cleaned):
    assert UtilsDNA.clean_string(dna_string) == dna_string_cleaned


