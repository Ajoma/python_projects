#!/usr/bin/env python3
'''
CPRG 100 Course, Assignment #:4 Sky Diving
Created by: Emmanuel Ajoma
Date: 24-06-2021
'''

'''
All constants are highlighted here.
'''
MAIN_CHUTE_KG = 11
EMERGENCY_CHUTE_KG = 9
MAX_CHUTE_CAN_HANDLE_KG = 105
MAX_BODY_WEIGHT_KG = 105 -(11+9) #85kg
MAX_HEIGHT_CM = 182

def file_list(): 
    '''
    Ask the user for a filename. Opens the file and splits the data in a list.
    '''
    done = True
    while done:
        done = False
        file_name = input("\nWhat is your file name? (Enter 'jumpers.txt' as filename): ")
        if file_name[-4:] != ".txt":
            print("Invalid entry! Enter a file name with a .txt extension")
            done = True

    fname = open (file_name, 'r')
    text = fname.read()
    fname.close()

    jumpers_list = text.split()
    del jumpers_list[0:3] # first 3 items are "name", "weight", "height" so not needed
    # print("jumpers_list:\n", jumpers_list)
    # print("\njumpers_list:\n", jumpers_list)

    file_dict(jumpers_list)

def file_dict(jumpers_list):
    '''
    Makes the list into key/value pairs each for height and weight dictionaries.
    '''
    dict_weights = {}
    dict_heights = {}

    i=0
    while (i < (len(jumpers_list)-2)):
        dict_weights.update({jumpers_list[i]:jumpers_list[i+1]})
        dict_heights.update({jumpers_list[i]:jumpers_list[i+2]})
        i+=3

    # print("\ndict_weights:\n", dict_weights)
    # print("\ndict_heights:\n", dict_heights)
    '''
    Each jumpers body weight is converted to an integer and added to the main and emergency chutes.
    Total weight should not exceed 105kg.
    Height is converted to an integer and should not exceed 182cm.
    '''
    for key, value in dict_weights.items():
        value = int(value) + MAIN_CHUTE_KG + EMERGENCY_CHUTE_KG
        dict_weights.update({key:value})

    for key, value in dict_heights.items():
        value = int(value)
        dict_heights.update({key:value})
    '''
    Keeps the maximum total weight of 500kg in check by choosing who meets the criteria 
    to skydive and who does not. 
    '''
    while sum(dict_weights.values()) > 500:
        heaviest_guy = max(dict_weights, key=dict_weights.get)
        del dict_weights[heaviest_guy]
        print("\n==================================================")
        print(heaviest_guy, ": Sorry, you're too heavy. You'd need a military chute T10 to jump!", sep="")
    
    if sum(dict_weights.values()) < 500:
        for key, value in dict_weights.items():
            if value < MAX_CHUTE_CAN_HANDLE_KG:
                if dict_heights.get(key) < MAX_HEIGHT_CM:
                    print(key, ": You are okay to jump.", sep="")
                elif dict_heights.get(key) >= MAX_HEIGHT_CM:
                    print(key, ": Sorry, you're too tall and cannot jump today!", sep="")
            elif value > MAX_CHUTE_CAN_HANDLE_KG:
                print(key, ": Sorry, you're too heavy. You'd need a military chute T10 to jump", sep="")
        '''
        To determine the lightest person to wear the video camera
        '''
        lightest_guy = min(dict_weights, key=dict_weights.get)
        if dict_heights.get(lightest_guy) < MAX_HEIGHT_CM:
            print(lightest_guy, ": You're the designated carrier of the video camera for this jump!", sep="")
            print("==================================================\n")
    else:
        print("Sorry, you Cannot fly today! The maximum airplane weight has been exceeded.", sep="")


file_list()
    
