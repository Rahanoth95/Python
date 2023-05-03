# Asks the buyer for their age.
Age = int(input("Welcome to the movies! What is your age? You may be eligible for discount. \n"))
# This implements the costs of tickets.
Children_ticket = 6
Adult_ticket = 10
Senior_ticket = 5
# Tell's them the cost of ticket if they are within the correct age range.
if Age <= 14: print("The child ticket costs $", Children_ticket)
if Age >= 62: print("The senior tickets are discounted too $", Senior_ticket)
# Gives a range in-between the age 15+ and 61 and below for an adult ticket
if (Age >= 15) and (Age <= 61): print("The adult ticket costs $", Adult_ticket)
# Asks The user if the movie they are going to watch is 3D
Three_D = input("Is the movie your going to watch 3D? It will cost more. \n")
# Adds a surcharge for the movie being 3D
Three_D_Surcharge = 4
# If the movie they want is in 3D adds the surcharge and tells the user.
if Three_D == "Yes":
    if Age >= 62:
        print("The Senior tickets for 3D movies cost $", Senior_ticket + Three_D_Surcharge)
    elif Age > 14:
        print(
            "The adult ticket for 3D costs $", Adult_ticket + Three_D_Surcharge)
    else:
        print(
            "The children's ticket for 3D costs $", Children_ticket + Three_D_Surcharge)
    # If the user says the movie is not in 3D there is no price change to the ticket and tells them
        else:
        print("The price does not change.")
