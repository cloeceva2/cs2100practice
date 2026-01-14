"""
Example approaches to dealing 
with invalid user input
"""

from typing import Optional

import unittest
from unittest.mock import patch, Mock

#########################

PROMPT: str = "Please enter your age: "

def get_age_a() -> int:
    """
    Gets user's age

    Returns
    =======
    int
        Supplied age

    Raises
    ======
    ValueError
        The supplied age was not
        an integer
    """
    return int(input(PROMPT))

# usage
# try:
#     print(f"Wow: {get_age_a()}")
# except ValueError:
#     print(":(")


def get_age_b() -> Optional[int]:

    #qualifier of a type -- optional
    #only returns if the value is the right type 
    #capitalization matters

    """
    Gets user's age

    Returns
    =======
    Optional[int]
        Supplied age in int , or None if
        not supplied an integer
    """
    try: # is how you run code that might throw an error 
        return int(input(PROMPT)) # if works and value is an int then returns the age 
    except ValueError: # if not an int returns nothing because value is not an int 
        return None

# usage
# age: Optional[int] = get_age_b()
# if age:
#     print(f"Wow: {age}")
# else:
#     print(":(")


def get_age_c() -> int:
    """
    Gets user's age, retrying
    upon non-integer input
    or an integer less than 1

    Returns
    =======
    int
        Valid age
    """

    age: int = -1
    while age < 1:
        try:
            age = int(input(PROMPT))
        except ValueError:
            age = -1

    return age

# usage
# print(f"Wow: {get_age_c()}")


#########################

class TestBadStuff(unittest.TestCase):
    """
    Tests for when bad things happen
    """

    @patch('builtins.input', side_effect=['2'])
    def test_a_good(self, _: Mock) -> None:
        """Valid test for version a"""
        self.assertEqual(get_age_a(), 2)

    @patch('builtins.input', side_effect=['-2'])
    def test_a_neg(self, _: Mock) -> None:
        """Negative test for version a"""
        self.assertEqual(get_age_a(), -2)

    @patch('builtins.input', side_effect=['forty'])
    def test_a_bad(self, _: Mock) -> None:
        """Bad input test for version a"""
        with self.assertRaises(ValueError):
            get_age_a()

    ###

    @patch('builtins.input', side_effect=['2'])
    def test_b_good(self, _: Mock) -> None:
        """Valid test for version b"""
        self.assertEqual(get_age_b(), 2)

    @patch('builtins.input', side_effect=['-2'])
    def test_b_neg(self, _: Mock) -> None:
        """Negative test for version b"""
        self.assertEqual(get_age_b(), -2)

    @patch('builtins.input', side_effect=['forty'])
    def test_b_bad(self, _: Mock) -> None:
        """Bad input test for version b"""
        self.assertIsNone(get_age_b())

    ###

    @patch('builtins.input', side_effect=['2'])
    def test_c_good(self, _: Mock) -> None:
        """Valid test for version c"""
        self.assertEqual(get_age_c(), 2)

    @patch('builtins.input', side_effect=['-2', '42'])
    def test_c_neg(self, _: Mock) -> None:
        """Negative test for version c"""
        self.assertEqual(get_age_c(), 42)

    @patch('builtins.input', side_effect=['forty', '40'])
    def test_c_bad(self, _: Mock) -> None:
        """Bad input test for version c"""
        self.assertEqual(get_age_c(), 40)

if __name__ == "__main__":
    unittest.main()
