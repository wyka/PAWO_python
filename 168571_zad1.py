import random

def my_code():
	"""funkcja generuje kod"""
	
	pool=[1,2,3,4]
	random.shuffle(pool)
	return pool
   
my_code()

black="+" # wlasciwa pozycja i wlasciwa liczba
white="0" # wlasciwa liczba, ale niewlasciwa pozycja
neitherBlacknorWhite="-" # niewlasciwa pozycja i liczba

blacks=0 # licznik trafien, max=4

def your_move():
	
	"""funkcja ocenia Twoj ruch"""
	
	pool=my_code()
	
	excluded=[5,6,7,8,9,0]
	
	print "\n\tGraczu, podaj swoj kod jako czterocyfrowa liczbe zlozona \n\tz cyfr od 1 do 4!"
	print "\tPamietaj, ze kazda z cyfr mozesz wykorzystac tylko raz!\n"
	
	for j in range(1,11):
		guess=input()
		print "\n"
		guessListed=map(int,str(guess))
	
		total=sum(guessListed) # jesli nalezy wykorzystac kazda z cyfr dokladnie raz to ich suma zawsze wynosi 10
	
		if guessListed==pool:
			print "\nJestes zwyciezca! \o/\n"
			if j<=3:
				score=11-j
				print "Twoj wynik to: ",score," punktow\n"
				return 0

		if any(set(guessListed).intersection(excluded)):
			check=10

		if guess>4321 or guess<1234 or total!=10 or check==10:
			print "Bledna liczba!\n"
			
		else:		
			for i in range(0,4):
				if guessListed[i]==pool[i]:
					print black,
					blacks=i
				elif guessListed[i] in pool:
					print white,
				else:
					print neitherBlacknorWhite,
						
			print "\n"
				
		if j<10:
			attempts=10-j
			print "Zostalo Ci:",attempts," prob\n"
						
		elif j==10:
			print "Szyfr to: ",pool
			print "\n'Game over!' \n\t~Paulo Coelho\n"
			return 0
				
your_move()

if __name__=='__main__':
	your_move()
