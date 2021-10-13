#body mass index



def bmi():

	print("""
 __   ____  
||>) ||\/|| ||
||>) ||  || || calculator

	""")
  
	while True:
	  
		a=float(input("input ur body mass: "))

		b=float(input("\ninput ur height: "))

		print(f'\n[-_-] = ur bmi result is {a/b**2}')
	  
		if a/b**2 >= 18.5 and a/b**2 <= 30:
			 print('good\n')
			 
		elif a/b**2 <= 18.5:
			 print('under weight\n')
			 
		elif a/b**2 >= 30:
			 print('over weight\n')

		else:
		   print("")



		con = int(input("\nif u want to calculate BMI again press : 1 \nto exit : press any other no key\n: "))


		if con == 1:
		  print("\n-----------next-------------\n")

		elif con != 1:
		   	return """you exit from BMI calculator\n\n
		   	        
               ^^^^  |  ^^^^          
    <--------------[^_^]-------------->""" 
		   	break 
		  
	




























