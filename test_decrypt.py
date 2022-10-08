"""
A sample test case for Finding the Key.
Feel free to add more!
"""

import pytest
from io import StringIO
from decrypt import decrypt

def test_passage() -> None:
    """Test a two-line passage."""
    passage = '''Q svme pm nmtb smmvtg bpm ijamvkm wn pqa
wev niuqtg.'''
    decrypted = '''i knew he felt keenly the absence of his
own family.'''
    assert decrypt(StringIO(passage), 'wordlist.txt') == decrypted

if __name__ == "__main__":

    pytest.main(["test_decrypt.py"])
