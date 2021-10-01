"""Module to combine all faces."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Combine:
    """Combine class."""

    def sides(self, sides):
        """Join all the sides together into one single string.

        :param sides: dictionary with all the sides
        :returns: string
        """
        combined = ''
        for face in 'URFDLB':
            combined += ''.join(sides[face])
        return combined


combine = Combine()
