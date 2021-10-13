#velocity calculator



def velocity():
	print('''
	                 ^^^^^^^^^
 \=    =/ ||!!!!!  ||      _____
  \=__=/  |*       |*      || ||
   \==/   |****    |*      || ||
    \/    |*       ||_*_|  || ||
    <>    #######  ######  ##city calculator  
	''')
	while True:
		distance=int(input("distance of the object moved: "))#the dis taken
		time=int(input("\nthe time it takes to the obj to reach to its destination in sec: ")) #where the time is taken
		print(f'\n[-_-] = {distance/time}m/s')
		


		cont = int(input("\nif u want to calculate velocity again press : 1 \nto exit : press any other no key\n: "))


		if cont==1:
			print("\n-----------next-------------\n")

		elif cont != 1:
		   	return """you exit from Velocity calculator\n\n
               ^^^^  T  ^^^^          
    <--------------[^_^]-------------->""" 
		
		  