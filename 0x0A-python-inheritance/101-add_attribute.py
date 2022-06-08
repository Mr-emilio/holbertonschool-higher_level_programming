#!/usr/bin/python3
""" module for add_attribute function"""



def add_attribute(obj, attribute, value):
    """add_attribute function"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
