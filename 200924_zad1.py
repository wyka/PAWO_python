# -*- coding: utf-8 -
import random

X = (1,2,3,4,5,6)

def createKey() :
	Key = (random.choice(X),random.choice(X),random.choice(X),random.choice(X))
	return Key
	
def checkSequence(Key, Sequence) :
	var = 0
	var2 = 0
	for i in range (0,4) :	
		if (Key[i] == Sequence[i]) :
			var += 1
		if (Sequence[i] in Key) :
			var2 += 1
	return [var,var2]
	
def inputSequence() :
	input = ""
	seq = [0,0,0,0]
	while (len(input) != 4 or Error > 0) :
		input = raw_input()
		Error = 0
		if (len(input) == 4) :
			for i in range(0,4) :
				try :
					seq[i] = int(input[i])
				except ValueError :
					Error+=1
			if (Error > 0) : 
				print "Wprowadzona sekwencja jest niepoprawna, spróbuj ponownie: "
		else :
			print "Sekwencja ma niepoprawną długość, spróbuj ponownie: "
	return seq
				
Key = createKey()
limit = 0
var = 0

print "\nWitaj w grze Mastermind!"
while (var != 4 ) :
	print "Wprowadź sekwencję czterech cyfr [1-6]: "
	if (limit <= 10) :
		seq = inputSequence()
		var = checkSequence(Key,seq)
		if (var[0] == 4) :
			print "Odgadłeś całą sekwencję, gratulacje !!!"
		else :
			print "Liczba cyfr na właściwych miejscach = ", var[0]
			print "Liczba cyfr które znajdują się w kluczu = ", var[1]
			print Key
	else :
		print "Niestety nie udało Ci się odgadnąć klucza :( ", Klucz
		break
	limit += 1