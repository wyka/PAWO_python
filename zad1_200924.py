# -*- coding: utf-8 -
"""Mastermind Game"""
import random

X = (1, 2, 3, 4, 5, 6)

def create_key():
    """ Creates key """
    key = (random.choice(X), random.choice(X),
	        random.choice(X), random.choice(X))
    return key
	
def check_sequence(key, sequence_after_conversion):
    """ Check if key is correct """
    in_key = 0
    in_key_in_position = 0

    for one_of_key, one_of_seq in zip(key, sequence_after_conversion):
        if (one_of_key == one_of_seq):
            in_key_in_position += 1
        elif (one_of_seq in key):
            in_key += 1
    return in_key, in_key_in_position		
	
def input_sequence():
    """ Converse user input to list """
    user_input = ""
    sequence = [0, 0, 0, 0]
    error = 0
    while (len(user_input) != 4 or error > 0):
        user_input = raw_input()
        error = 0
        if (len(user_input) == 4):
            for i in range(0, 4):
                try:
                    sequence[i] = int(user_input[i])
                except ValueError:
                    error += 1
            if (error > 0): 
                print "Wprowadzona sekwencja jest niepoprawna,"
                print "spróbuj ponownie:"		        
        else:
            print "Sekwencja ma niepoprawną długość, spróbuj ponownie: "
    return sequence
				
KEY = create_key()
LIMIT = 0
IN_KEY = 0
IN_KEY_IN_POSITION = 0

print "\nWitaj w grze Mastermind!"
while (IN_KEY_IN_POSITION != 4 ):
    print "Wprowadź sekwencję czterech cyfr [1-6]: "
    if (LIMIT <= 10):
        SEQUENCE_AFTER_CONVERSION = input_sequence()
        IN_KEY, IN_KEY_IN_POSITION = check_sequence(KEY,
                                            		SEQUENCE_AFTER_CONVERSION)
        if (IN_KEY_IN_POSITION == 4):
            print "Odgadłeś całą sekwencję, gratulacje !!!"
        else:
            print "Liczba cyfr na właściwych miejscach = ", IN_KEY_IN_POSITION
            print "Liczba cyfr które znajdują się w kluczu = ", IN_KEY
    else:
        print "Niestety nie udało Ci się odgadnąć klucza :( ", KEY
        break
    LIMIT += 1