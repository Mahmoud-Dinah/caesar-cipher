from caesar_cipher.caesar_cipher import *

def test_encrypt_a_string_with_a_given_shift():
    assert encrypt("It was the best of times, it was the worst of times.", 5) == "Ny bfx ymj gjxy tk ynrjx ny bfx ymj btwxy tk ynrjx"

def test_decrypt_a_previously_encrypted_string_with_the_same_shift():
    assert decrypt("Ny bfx ymj gjxy tk ynrjx ny bfx ymj btwxy tk ynrjx", 5) == "It was the best of times it was the worst of times"

def test_encryption_should_handle_upper_and_lower_case_letters():
    assert encrypt('TeSt LoWeR AnD UPpEr Case',2) == "VgUv NqYgT CpF WRrGt Ecug"


### encryption should allow non-alpha characters but ignore them, including white space
def test_ignore_non_alpha_and_whiteSpace():
  assert encrypt('  #$@#$@#$ TT !@#!@#%^^&%^&',2) == "   VV "