"""
Some extra practice!!
"""

from typing import Optional

import random

import unittest
from unittest.mock import Mock, call, patch

##########################################
# Questions
##########################################

"""
1. Write a Python main function that prints “hello world!” - now test it!
"""

"""
2. Consider this function that prompts a user for their dog's age.

def func() -> Optional[int]:
     age = int(input("Enter age\n"))
     if age < 0:
           return None
     return age

a) Write a docstring for this function
b) What would happen if the user entered -2?
c) What would happen if the user entered "forty-seven"?
"""

"""
3. In order to work on and submit your HW/Labs this semester, 
   you need to use the following git commands: 
   
        git add
        git clone
        git push
        git commit
        
    Write the commands below in the order you would expect to use them.
"""

"""
4. Finish the function below (including the docstring!): 
   keep generating random numbers until you get one that exists in lst;
   return the number of calls to randint that were necessary.

def func2() -> int:
    good_nums = [3, 4, 5, 6]
    rand_num = random.randint(1, 10)
    ...
"""

"""
5. What does the Python snippet below print?

i = 1
while i < 3:
    print(i * 2)
    i = i + 1
"""

"""
6. What does the Python snippet below print?
s = "python"
for letter in s:
	print(letter.upper())
"""

"""
7. Finish the Python code below: 
* Add the key/value pair "c", 3 to the dictionary
* Print out all key/value pairs using a loop
* Return the final dictionary
* Document the function

def func7() -> dict[str, int]:
    dct = {"a" : 1, "b" : 2}
    ...
"""

"""
8. Write a documented function named list_sum that...
   * takes in a list of ints
   * returns an int, the sum of all values in the list

   Do NOT call Python's built-in sum() method. You can assume the list is non-empty.
"""

"""
9. Now TEST the function in #8
"""

"""
10. Write & test a documented function named dict_sum that...
* takes in a dictionary of string : int pairs; or possibly None
* returns an int, the sum of all values in the list; or None if there was no supplied dictionary

    Do NOT call Python's built-in sum() method. Assume the dictionary is NOT empty.
"""

##########################################
# Sample Solutions 
# (below, 🙈 until ready!!)
##########################################









































"""
3. Typical git command sequence...

git clone <- copies a remote repo to your local machine
git add <- after changes in the work area, stage
git commit <- commit staged changes to your local repo
git push <- push local commits back to the remote repo
"""

def func() -> Optional[int]:
    """
    Gets a dog's age

    Returns
    =======
    Optional[int]
        age in years, or None
        if below zero

    Raises
    ======
    ValueError
        Non-integer input
    """
    age = int(input("Enter age\n"))
    if age < 0:
        return None
    return age

def func2() -> int:
    """
    Returns how many calls to
    randint were needed to find
    a number within good_nums
    """
    good_nums: list[int] = [3, 4, 5, 6]
    counter: int = 1
    rand_num: int = random.randint(1, 10)

    while rand_num not in good_nums:
        counter += 1
        rand_num = random.randint(1, 10)

    return counter


def func7() -> dict[str, int]:
    """
    Adds a key-value pair to
    a starting dictionary and
    then prints it out and
    returns it
    """

    dct: dict[str, int] = {"a" : 1, "b" : 2}
    dct['c'] = 3

    for k,v in dct.items():
        print(f'{k}={v}')

    return dct


def list_sum(list_of_nums: list[int]) -> int:
    """
    Adds all the numbers in the list

    Parameters
    ==========
    list_of_nums: list[int]
        supplied list of numbers,
        assumed to be non-empty

    Returns
    =======
    int
        sum of the numbers in
        the supplied list
    """
    sum_of_nums: int = 0

    for num in list_of_nums:
        sum_of_nums += num

    return sum_of_nums


def dict_sum(d: Optional[dict[str, int]]) -> Optional[int]:
    """
    Produces the sum of the values
    in the supplied dictionary, or None

    Parameters
    ==========
    d: Optional[dict[str, int]]
        non-empty string-integer pairs, or None

    Returns
    =======
    Optional[int]
        sum of the dictionary values, or None
    """

    if d is None:
        return None

    d_sum: int = 0
    for num in d.values():
        d_sum += num

    return d_sum


class TestExtra(unittest.TestCase):
    """
    Tests for all the extra problems!
    """

    @patch("builtins.print")
    def test_main(self, mock_print: Mock) -> None:
        """Tests main"""
        main()

        mock_print.assert_has_calls([
            call("hello world!")
        ])

    @patch("builtins.input", side_effect=["-2"])
    def test_func_neg(self, _: Mock) -> None:
        """Tests func with -2"""
        self.assertIsNone(func())

    @patch("builtins.input", side_effect=["forty-seven"])
    def test_func_words(self, _: Mock) -> None:
        """Tests func with forty-seven"""
        with self.assertRaises(ValueError):
            func()

    @patch("random.randint", side_effect=[3])
    def test_func2_immediate(self, _: Mock) -> None:
        """Tests func2 with an immediate good number"""
        self.assertEqual(func2(), 1)

    @patch("random.randint", side_effect=[1, 7, 8, 2, 6])
    def test_func2_delayed(self, _: Mock) -> None:
        """Tests func2 with a delayed good number"""
        self.assertEqual(func2(), 5)

    @patch("builtins.print")
    def test_prob5(self, mock_print: Mock) -> None:
        """Tests output from prob 5"""

        i = 1
        while i < 3:
            print(i * 2)
            i = i + 1

        mock_print.assert_has_calls([
            call(2),
            call(4),
        ])

    @patch("builtins.print")
    def test_prob6(self, mock_print: Mock) -> None:
        """Tests output from prob 6"""

        s = "python"
        for letter in s:
            print(letter.upper())

        mock_print.assert_has_calls([
            call('P'),
            call('Y'),
            call('T'),
            call('H'),
            call('O'),
            call('N'),
        ])

    @patch("builtins.print")
    def test_func7(self, mock_print: Mock) -> None:
        """Tests func7"""

        self.assertDictEqual(
            func7(),
            {'a': 1, 'b': 2, 'c': 3}
        )

        mock_print.assert_has_calls([
            call('a=1'),
            call('b=2'),
            call('c=3'),
        ])

    def test_list_sum_single(self) -> None:
        """Tests list_sum with a single list entry"""
        self.assertEqual(list_sum([1]), 1)

    def test_list_sum_multiple(self) -> None:
        """Tests list_sum with multiple numbers"""
        self.assertEqual(list_sum([-1, 0, 5]), 4)

    def test_dict_sum_none(self) -> None:
        """Tests dict_sum with a None supplied"""
        self.assertIsNone(dict_sum(None))

    def test_dict_sum_single(self) -> None:
        """Tests dict_sum with a single entry supplied"""
        self.assertEqual(dict_sum({'a': 1}), 1)

    def test_dict_sum_multiple(self) -> None:
        """Tests dict_sum with multiple entries supplied"""
        self.assertEqual(
            dict_sum({'z': -1, 'foo': 0, 'A': 10}), 
            9
        )


def main() -> None:
    """
    Question #1
    (though below we'd
    call main() instead of
    the unit tests)
    """
    print("hello world!")

if __name__ == "__main__":
    unittest.main()
