#pressure calculator



def pressure():
	print('''
  
  ||!!!!||  ******    !!!!!!!
  ||    ||  **    *   **
  ||||||||  ******    !!!!!
  ||        **  **    !!!!!
  ||        **   **   **
  ||        **    **  !!ssure  calculator 
	''')
	while True:
		force=int(input("force of the object: "))#the force taken
		area=int(input("\nthe area of the obj: ")) #where the area is taken
		print(f'\n[-_-] = {force/area}pa')


		cont = int(input("\nif u want to calculate pressure again press : 1 \nto exit : press any other no key\n: "))


		if cont==1:
			print("\n-----------next-------------\n")

		elif cont != 1:
		   	return """you exit from pressure calculator\n\n
               ^^^^  T  ^^^^          
    <--------------[^_^]-------------->""" 
		