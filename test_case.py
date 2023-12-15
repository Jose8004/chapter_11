import pytest
import unittest
from main import validate_password
 
class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        assert validate_password("A1b2C3d4!")
        assert validate_password("R2$d5@Fg!")
    
    def test_empty_password(self):
        self.assertEqual(validate_password(""), "")
    
    def test_proper_length_password(self):
        assert validate_password("1Ab$") != True
        assert validate_password("1aB4$6789") == True
        assert validate_password("1aB4$67") == False
    
    def test_has_special_character(self):
        assert validate_password("Ab3456789") != True
        assert validate_password("Ab345678$") == True
    
    def test_has_a_digit(self):
        assert validate_password("Abcefghijklm$") == False
        assert validate_password("Abcefg123klm$") == True
    
    def test_has_upper(self):
        assert validate_password("abcde1234$") != True
        assert validate_password("ABCde1234$") == True
    
    def test_has_lower(self):
        assert validate_password("ABCDE1234$") == False
        assert validate_password("AbcdE1234$") == True
 
#ADD additional test cases as part of this question!
 
if __name__ == '__main__':
    pytest.main()