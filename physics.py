# every programe we wrote runs from here

from velocity import velocity
# velocity.velocity()

from force import force
#force.force() 


from acceleration import acceleration 
# acceleration.acceleration()


from pressure import pressure
#pressure.pressure()

from bmi import bmi
# bmi.bmi()

#-------------------------------------------


print("""          
        |######| ||    ||  \    //    =====   ********    *******    ===== 
        ||     | ||    ||   \  //    ***         ||      ***       ***
        |######| ||####||    \//      **         ||      **          **
        ||       ||****||    //         **       ||      **            **
        ||       ||    ||   //            **     ||      ***             **
        ||       ||    ||  //         =====    =======    *******   ===== calculator   #by boys at AASTU 

  """)


#----------------------------------------------



while True:

  a=input("""\nwelcome to phy calculator what do u want to calculate ?\n 
input ==> 1: for FORCE
       => 2: for VELOCITY
       => 3: for ACCELERATION
       => 4: for BMI
       => 5: for PRESSURE
       => 6: to quit  
ur input is: """)



  if int(a)==1:
    print(force.force())   #FORCE 
    


  elif int(a)==2:
    print(velocity.velocity()) #VELOCITY


  elif int(a)==3:
    print(acceleration.acceleration())   #ACCELERATION 


  elif int(a)==4:
    print(bmi.bmi()) #BMI


  elif int(a)==5:
    print(pressure.pressure()) #PRESSURE    


  elif int(a)==6:
    print("Thank u for using our product #boys") #EXIT
    break
        
        
  else:
    print("sorry u input a wrong data") 
    break
  

