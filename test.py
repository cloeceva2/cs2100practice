import unittest 
from unittest.mock import patch, Mock
# could also do import main but this is generally bad form 
# as it importas a large thing that you may not need
from main import ( # parenthese allows you to make long lists 
    greet_person, 

    is_cold_f
    # enumerating specific funtions 
)

class TestMainApp(unittest.TestCase):
    @patch('builtins.input', side_effect=["alice"])
    @patch('builtins.print') # fake what happends anytime it runs greetperson
    def test_greetperson(self) -> None:
        "Say hello to alice"
        greet_person()
        expected_calls = [
            unittest.mock.call("howdy, alice")
        ]
        mock_print.assert_has_calls(expected_calls)  
           
# starting poiint 


def test_iscoldf_70(self) -> None:
    "test is_cold_f for 70"
    self.assertFalse(is_cold_f(70))

def test_iscoldf_68()-> None:
    "test is_cold_f for 68"
    self.assertTrue(is_cold_f(68))

def test_iscoldf_freezing(self) -> None:
    "test is_cold_f for 32"
    self.assertTrue(is_cold_f(32))

def test_iscoldf_boling(self) -> None:
    "test is_cold_f for 212"
    self.assertFalse(is_cold_f(212))

    
if __name__ == "__main__":
    unittest.main()