def newCalculator():
	
	while True:
		operator=raw_input("\nPodaj operator dzialania, ktore chcesz wykonac\n")
		var=raw_input("\nWpisz liczby oddzielone spacja\n").split()
		
		for i in range(0,len(var)):
			var[i]=var[i].replace(',','.')
			
		ans=str(eval(operator.join(var))).replace('.',',')
		print "\nWynik: ",ans
		
newCalculator()
