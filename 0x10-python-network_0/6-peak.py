#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak in the list.
    """

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
