#!/usr/bin/env python3
'''
Stanford Code in Place 
Final Project: QATAR 2022 -- FIFA WORLD CUP CHAMPIONSHIPS
Created by: Emmanuel Ajoma
Date: 22-06-2021
'''

print("*** Tickets for FIFA World Cup Championship ***\n")
stage_choice = True
while stage_choice:
    print("There are five(5) stages of the World Cup Championship to choose from:")
    print("=======================================================================")
    print("Choose a: for Group stage")
    print("Choose b: for Round of 16 stage")
    print("Choose c: for Quarterfinals stage")
    print("Choose d: for Semifinals stage")
    print("Choose e: for Final stage")
    print("=======================================================================")

    stage_category = input("Please enter your stage category: a, b, c, d, or e = ")
    if stage_category == 'a' or stage_category == 'b' or stage_category == 'c' or stage_category == 'd' or stage_category == 'e':
        if stage_category == 'a':
            print("Your stage category selected is: Group stage\n")
            print("For Group stage, available seat categories and price points are:")
            print("=======================================================================")
            print("a: Standard seat = $40")
            print("b: Premium seat = $80")
            print("c: VIP seat = $200")
            print("=======================================================================")
        elif stage_category == 'b':
            print("Your stage category selected is: Round of 16 stage\n")
            print("For Round of 16 stage, available seat categories and price points are:")
            print("=======================================================================")
            print("a: Standard seat = $60")
            print("b: Premium seat = $160")
            print("c: VIP seat = $400")
            print("=======================================================================")
        elif stage_category == 'c':
            print("Your stage category selected is: Quarterfinals stage\n")
            print("For Quarterfinals stage, available seat categories and price points are:")
            print("=======================================================================")
            print("a: Standard seat = $80")
            print("b: Premium seat = $160")
            print("c: VIP seat = $400")
            print("=======================================================================")
        elif stage_category == 'd':
            print("Your stage category selected is: Semifinals stage\n")
            print("For Semifinals stage, available seat categories and price points are:")
            print("=======================================================================")
            print("a: Standard seat = $140")
            print("b: Premium seat = $280")
            print("c: VIP seat = $700")
            print("=======================================================================")
        else:
            print("Your stage category selected is: Final stage\n")
            print("For Final stage, available seat categories and price points are:")
            print("=======================================================================")
            print("a: Standard seat = $240")
            print("b: Premium seat = $480")
            print("c: VIP seat = $1200")
            print("=======================================================================")
        stage_choice = False
    else:
        print("Error: Valid entry is ONLY a, b, c, d, or e\n")
# print("\nYour stage category selected is: ", stage_category)
#Validating the stage_category loop

seat_choice = True
while seat_choice:
    # if stage_category == 'a': #Group stage
    seat_category = input("Please enter your seat category: a, b, or c = ")
    if seat_category == 'a' or seat_category == 'b' or seat_category == 'c':
        if seat_category == "a": #Standard
            print("Your seat category selected is: Standard\n")
        elif seat_category == "b": #Premium
            print("Your seat category selected is: Premium\n")
        else:   #VIP
            print("Your seat category selected is: VIP\n")
        seat_choice = False
    else:
        print("\nError: Valid entry is ONLY a, b, or c\n")
# print("Your seat category selected is: ", seat_category)

#Number of ticket sales 
while True:
    try:
        number_of_tickets = int(input("How many tickets do you wish to buy today? "))
        break
    except:
        print("Error: Valid entry has to be a number: \n")

#price_point categories 
if seat_category == 'a':  #Standard
    ticket_price_point = 40
elif seat_category == 'b': #Premium
    ticket_price_point = 80
else:
    ticket_price_point = 200 #VIP
# print("Cost per seat = $", price_point, sep="")

# Print price points based on stages
if stage_category == "a": #Group stage
    ticket_price_point = ticket_price_point
    print("Group stage cost per seat = $", ticket_price_point, sep="")
elif stage_category == "b": #Round of 16 stage
    ticket_price_point = ticket_price_point * 1.5
    print("Round of 16 stage cost per seat = $", ticket_price_point, sep="")
elif stage_category == "c": #Quarterfinals stage
    ticket_price_point = ticket_price_point * 2
    print("Quarterfinals stage cost per seat = $", ticket_price_point, sep="")
elif stage_category == "d": #Semifinals stage
    ticket_price_point = ticket_price_point * 3.5
    print("Semifinals stage cost per seat = $", ticket_price_point, sep="")
else:  #Finals stage
    ticket_price_point = ticket_price_point * 6
    print("Final stage cost per seat = $", ticket_price_point, sep="")
    
total_ticket_cost = number_of_tickets * ticket_price_point
if number_of_tickets > 20:
    total_ticket_cost = number_of_tickets * ticket_price_point * 0.90
    print("Yay, you're eligible for a 10", "%", " discount!", sep="")
elif number_of_tickets > 10:
    total_ticket_cost = number_of_tickets * ticket_price_point * 0.95
    print("Yay, you're eligible for a 5", "%", " discount!", sep="")
else:
    print("You're not eligible for a discount!\n")

print("The total cost for your ", number_of_tickets, " tickets is: $", total_ticket_cost, sep="")
print("\n*** Thank you for your order today!! ***")

        















