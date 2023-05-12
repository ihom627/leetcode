#!/usr/bin/env python


test_numbers = [1, 4, 5, 7, 2, 3, 6, 8, 9]


def merge_sort(input_numbers):

    print "merge_sort() input %s " % input_numbers

    result = []

    #terminating condition
    if len(input_numbers) <= 1:
        return

    #divide in half
    first_half = input_numbers[0:len(input_numbers)/2]
    second_half = input_numbers[len(input_numbers)/2:len(input_numbers)]

    #print first_half
    #print second_half
  
    #now call merge_sort on each half
    merge_sort(first_half)
    merge_sort(second_half)
    result = sort(first_half, second_half) 



def sort(list1, list2):
    print "sort() %s %s" % (list1, list2)

    return_list = []
   
    i = 0
    j = 0

    #compare at beginning of the lists
    while i<len(list1) and j<len(list2):
        if (list1[i] <= list2[j]):
            return_list.append(list1[i])
            i += 1
        else:
            return_list.append(list2[j])
            j += 1

    #just stick on the rest of list1 
    while i < len(list1):
        return_list.append(list1[i])
        i += 1
      
    #just stick on the rest of list2 
    while j < len(list2):
        return_list.append(list2[j])
        j += 1
      
        
    print "return_list %s " % return_list
    return return_list



merge_sort(test_numbers)

