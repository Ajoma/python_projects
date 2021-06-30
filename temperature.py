#!/usr/bin/env python3
'''
CPRG 100 Course, Assignment #:3 Temperatures
Created by: Emmanuel Ajoma
Date: 24-06-2021
'''
def getDays():
    '''
    Shows the days of the week, starting from Sunday
    '''
    dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return dayList

def getTemps(dayList):
    '''
    Returns both high and low temperatures for the dayList 
    '''
    temp_list = []
    for day in dayList:
        done = True
        while done:
            low_temp = int(input("Enter low temperature for [" + day + "]: "))
            if low_temp <= 40 and low_temp >= -40:
                temp_list.append(low_temp)
                done = False
            else:
                print("Invalid! Enter a value between [-40 and 40].")

        done = True
        while done:
            high_temp = int(input("Enter high temperature for [" + day + "]: "))
            if high_temp <= 40 and high_temp >= -40:
                temp_list.append(high_temp)
                done = False
            else:
                print("Invalid! Enter a value between [-40 and 40].") 
    return temp_list 

def displayAverage(dayList, temps):
    '''
    Returns the average temperature per day in the dayList
    '''
    for i in range(len(dayList)):
        average_temp = (temps[2*i]+temps[2*i+1])/2
        print(dayList[i], average_temp)
    return average_temp

def main():
    '''
    Returns the week_days list, Low and high temperatures of the week
    Computes the average temperature of the days in the week.
    '''
    week_days = getDays()
    print("\nEnter temperatures:", week_days, "\n")
    print("===========================")
    temperature_list = getTemps(week_days)
    print("===========================")
    print("Temperature list is: ", temperature_list)
    print("\nThe average temperatures are: ")
    average_temperature = displayAverage(week_days, temperature_list)
    print("===========================")


if __name__ == '__main__':
    main()
            