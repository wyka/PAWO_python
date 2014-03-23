# -*- coding: utf-8 -
"""Mastermind Game"""
import random

def create_key():
    """ Creates key """
    available = (1, 2, 3, 4, 5, 6)
    key = (random.choice(available), random.choice(available),
	        random.choice(available), random.choice(available))
    return key
	
def check_sequence(key, seq_after_conv):
    """ Check if key is correct """
    in_key = 0
    in_key_in_pos = 0

    for one_of_key, one_of_seq in zip(key, seq_after_conv):
        if (one_of_key == one_of_seq):
            in_key_in_pos += 1
        elif (one_of_seq in key):
            in_key += 1
    return in_key, in_key_in_pos		
	
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

def main():
    """ Main function """
    key = create_key()
    limit = 0
    in_key = 0
    in_key_in_pos = 0

    print "\nWitaj w grze Mastermind!"
    while (in_key_in_pos != 4 ):
        print "Wprowadź sekwencję czterech cyfr [1-6]: "
        if (limit <= 10):
            seq_after_conv = input_sequence()
            in_key, in_key_in_pos = check_sequence(key, seq_after_conv)
            if (in_key_in_pos == 4):
                print "Odgadłeś całą sekwencję, gratulacje !!!"
            else:
                print "Liczba cyfr na właściwych miejscach = ", in_key_in_pos
                print "Liczba cyfr które znajdują się w kluczu = ", in_key
        else:
            print "Niestety nie udało Ci się odgadnąć klucza :( ", key
            break
        limit += 1

if __name__ == "__main__":
    main()