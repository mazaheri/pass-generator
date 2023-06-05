# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:29:52 2023

@author: Pourya Mazaheri
"""

import string
import random

# password generator
def generate_pass(digit):
    pull = ''
    for i in range(digit):
        pull += random.choice(string.ascii_letters)
    print(pull)
    

if __name__ == '__main__':
    try:
        digits = int(input('Enter an Integer ='))
    except:
        print('enter an integer')
    
    generate_pass(digits)
