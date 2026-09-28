import unittest
from unittest.mock import patch
import io

class TestWallAreaProgram(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_area_calculation(self, mock_stdout, mock_input):
        import main  # This runs the student's code

        output = mock_stdout.getvalue().strip().split('\n')

        self.assertIn("Calculate the area of a wall.", output[0])
        self.assertIn("Width is 2 m and height is 5 m.", output[1])
        self.assertIn("The wall will be 10 square meters.", output[2])

if __name__ == '__main__':
    unittest.main()
