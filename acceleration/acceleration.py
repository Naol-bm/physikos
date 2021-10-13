#acceleration calculator



def acceleration():
	print('''

    *       ****    **** 
   * *    **      ** 
  *===*   **      **
 *     *  **      **  eleration  calculator
*       *   ****    **** 
	''')
	while True:
		velocity=int(input("velocity of the object: "))#the velocity taken
		time=int(input("\nthe time it takes to the obj to reach to its destination in sec: ")) #where the time is taken
		print(f'\n[-_-] = {velocity/time}m/s²')
		


		cont = int(input("\nif u want to calculate acceleration again press : 1 \nto exit : press any other no key\n: "))


		if cont==1:
			print("\n-----------next-------------\n")

		elif cont != 1:
		   	return """you exit from acceleation calculator\n\n
               ^^^^  T  ^^^^          
    <--------------[^_^]-------------->""" 
		