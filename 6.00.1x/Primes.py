# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 11:17:12 2017

@author: lucas
"""

def genPrimes():
    prime1 = 2
    primes = []
    count = 0
    test = True
    while True:
        yield prime1
        if test:
            primes.append(prime1)
        test = False
        print(prime1)
        while test == False:
            prime1 += 1 
            for i in primes:
                if prime1%i != 0:
                    count += 1
                else:
                    break
                if count == len(primes):
                    test = True
                    count = 0