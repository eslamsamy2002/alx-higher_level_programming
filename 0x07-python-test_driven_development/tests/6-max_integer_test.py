#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test class for the max_integer() function.
    """

    def test_empty_list(self):
        """
        Test that an empty list returns None.
        """
        self.assertIsNone(max_integer([]), "result should be none")

    def test_only_one_element_in_list(self):
        """
        Test that the list returns the true element.
        """
        num = 30
        self.assertAlmostEqual(max_integer([num]), num, f"result should be {num}")

    def test_positives_list(self):
        """
        Test that the list returns the true element.
        """
        list_of_elements = [10, 550, 70, 90]
        self.assertAlmostEqual(
            max_integer(list_of_elements), 550, "result should be 550"
        )

    def test_negatives_list(self):
        """
        Test that the list returns the true element.
        """
        list_of_elements = [-20, -300, -40, -10]
        self.assertAlmostEqual(
            max_integer(list_of_elements), -10, "result should be -10"
        )

    def test_negatives_positives_list(self):
        """
        Test that the list returns the true element.
        """
        list_of_elements = [-20, 600, -40, 1]
        self.assertAlmostEqual(
            max_integer(list_of_elements), 600, "result should be 600"
        )

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [
                    0.00123,
                    0.457568,
                    0.02345,
                    0.23423434,
                    0.45675674,
                    0.678678,
                    0.867090,
                    0.74653,
                    0.5745375,
                ]
            ),
            0.86709,
        )
