#force calculator



def force():
	print('''
       
||**** ++++++  ******      ****   *******
||     ||  ||  **    *   **       ** 
||**** ||  ||  ******   **        ******
||     ||  ||  **  **   **        ******
||     ||  ||  **   **   **       ** 
||     ++++++  **    **    ****   ******* calculator 

	''')
	while True:
		acceleration=int(input("acceleration of the object in m/s²: "))#the dis taken
		mass=int(input("\nmass of the object in kg: ")) #where the time is taken
		print(f'\n[-_-] = {acceleration*mass}N')
		


		cont = int(input("\nif u want to calculate force again press : 1 \nto exit : press any other no key\n: "))


		if cont==1:
			print("\n-----------next-------------\n")

		elif cont != 1:
		   	return """you exit from force calculator\n\n
               ^^^^  T  ^^^^          
    <--------------[^_^]-------------->""" 
		