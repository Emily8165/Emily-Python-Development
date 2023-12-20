import unittest

from my_task_manager.my_task_manager import custom_filters


class TestFunc(
    unittest.TestCase
):  # inherriting here lets you get alot of differnet test cases here.
    def test_linebreak(self):  # this needs to start with the word test for it to run.
        # i want to test if a line break "/n" is at every nth (defined in function) line in a function.
        # Arrange
        testing_string = "this is a random test string for testing it is very long so that we can do a lot of testing on it. "
        num = 10
        # Act
        result = custom_filters.add_line_breaks(testing_string, num)

        # Assert
        for i in enumerate(result, start=1):
            if i[0] % num == 0:
                self.assertEqual(i[1], " ")

    def test_numbers(self):
        # Arrange
        expected = 5
        num1 = 1
        num4 = 4

        # Act
        actual = num1 + num4

        # Assert
        assert actual == expected


if __name__ == "__main__":  # if we run the model directly run the code in here.
    unittest.main()
