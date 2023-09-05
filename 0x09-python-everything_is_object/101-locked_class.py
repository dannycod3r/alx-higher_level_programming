#!/usr/bin/python3
"""Module supplies a LockedClass"""


class LockedClass:
    """LockedClass permits only first_name as attribute"""
    __slots__ = ['first_name']
