#!/usr/bin/env python3
'''
CPRG 100 Course, Assignment #2: GRADES
Created by: Emmanuel Ajoma
Date: 23-06-2021
'''
def get_grades():
    '''
    Asks the user for a list of grades (numbers)
    Returns a list contianing the grades.
    '''
    grade_list = []
    done = False
    while (not done):
        grade = int(input("Enter grade (-ve to stop): "))
        if grade < 0:
            done = True
            continue
        elif grade % 2 != 0:
            grade_list.append(grade)
    return grade_list

def print_grades(alist): #
    '''
    Prints all the values of the list passed in
    '''
    for i in alist:
        print(i)

def average(alist):
    '''
    Returns the average value of the list of grades
    '''
    if alist == []:
        print("")
    else:
        total = 0
        for i in alist:
            total += i 
        print("\nTotal grades in grade list is:", total)
        average_grade = total / len(alist)
        return average_grade
    

def maximum(alist):
    '''
    Returns the maximum value in the grade list
    '''
    max = 0
    for i in range(len(alist)):
        if alist[i] > max:
            max = alist[i]
    return(max)


def main():
    '''
    Computes the average and the maximum of a list of grades entered by the user.
    '''
    print("===========================")
    print("*** GRADES ***")
    print("===========================")
    grades = get_grades()
    print("\nGrade list = ", grades)
    print("\n===========================")
    print("\nGrade list contains: ")
    print_grades(grades)
    average_grade = average(grades)
    print("Length of grade list is:", len(grades))
    maximum_grade = maximum(grades)
    print("\nAverage grade is:", average_grade)
    print("Maximum grade is: ", maximum_grade)
    print("===========================")


if __name__ == '__main__':
    main()
            

