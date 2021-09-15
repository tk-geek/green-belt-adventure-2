print("hello welcome to the jungle survive if you can.")

print()

def  choice (health ,damage):
  print ("-----------------------------------------------")
  while health > 0: 
    print ("HP:", health )
    print("Attack:", damage)
    print ("----------------")
    
    direction = input("pick a direction r, l, u, d ")

    if (direction == "r") :                   
      print("you encountered a wild predator ")
      #begin attack or not
      attack_or_not = input("do you want to attack the predator or run away?")
      if(attack_or_not == "attack" or attack_or_not == "Attack" ):
       print("you attacked the predetor", damage,"damage. It Died")
       hp = 50
      elif(attack_or_not == "run" or attack_or_not == "Run") :
        print("the predetor caught and killed you.")
        #end attack or not
        damage = 55

    elif (direction == "u"):
      print("you  found a sword")
      #begin take it or leave it
      take_it_or_leave_it = input ("do you want to take the sword  or leave it ")
      if (take_it_or_leave_it.lower()  == "take"):
          print("you take it")
      elif(take_it_or_leave_it.lower() == "leave"):
          print("you left the sword")
    
    elif (direction == "l"):
      print("you found money !")
    
    elif (direction == "d"):
      print("you encountered a evil wizard ",damage,"to the wizard")
      print ("the wizard dies")
      #attack 
      attack_or_not = input (" do you want to attack the wizard or not ")
      if(attack_or_not.lower() == "attack"):
        print("you attacked the wizard")
      elif(attack_or_not == "not"): 
        print("you didn’t attack the wizard")

    else:
      print ("please put a valid choice the valid choices are r, l, u, d ")
   

choice(60,50)