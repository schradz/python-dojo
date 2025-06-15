import unittest
from unittest.mock import patch
import io
from dojo_challenge import *

def suppress_print(self):
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull

class TestDojoChallenges(unittest.TestCase):
    '''Tests for dojo_challenges.py'''
    @patch('builtins.input', return_value="easy")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_difficulty_easy(self, mock_stdout, mock_input):
        '''Does user input for easy'''
        user_difficulty = get_user_difficulty()
        self.assertEqual(user_difficulty, "easy")

    
    @patch('builtins.input', return_value="medium")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_difficulty_medium(self, mock_stdout, mock_input):
        '''Does user input for medium work'''
        user_difficulty = get_user_difficulty()
        self.assertEqual(user_difficulty, "medium")


    @patch('builtins.input', return_value="hard")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_difficulty_hard(self, mock_stdout, mock_input):
        '''Does user input for hard work'''
        user_difficulty = get_user_difficulty()
        self.assertEqual(user_difficulty, "hard")

    
    @patch('builtins.input', return_value="eay")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_difficulty_typo(self, mock_stdout, mock_input):
        '''Does user input with typo report error'''
        user_difficulty = get_user_difficulty()
        self.assertEqual(user_difficulty, "error")


if __name__ == "__main__":
    unittest.main()