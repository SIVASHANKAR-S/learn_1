'''
A simple test hello world program

Author : Siva
Date   : Aug 28, 2023

'''

from hello import hello,tata


def test_hello():
    """
    A simple test function to test the output of hello function

    Returns:
        bool : True if the output of hello function is "Hello, World!"
    """
    assert hello() == "Hello, World!"



def test_tata():
    """
    A simple test function to test the output of tata function

    Returns:
        bool : True if the output of hello function is "Hello, World!"
    """
    assert tata() == "Bye, World!"
