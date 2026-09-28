import unittest
from unittest.mock import patch
import io

class TestRemainderProgram(unittest.TestCase):
    @patch('builtins.input', return_value='521')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_remainder_output(self, mock_stdout, mock_input):
        import main  # This runs the student's code
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertEqual(output[0], "Value is 521")
        self.assertEqual(output[1], "The remainder is 1 when 521 is divided by 2.")

if __name__ == '__main__':
    unittest.main()

