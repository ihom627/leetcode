#!/usr/bin/env python

#this is a leet code exercise
#determine if there are any anagrams in a list

#approach is to create a dictionary and compare

test_list = ["cat", "tac", "leg", "gel", "don", "nod"]

def anagram(input_list):
    print input_list

    while input_list:

        #create master dictionary
        dictionary_master = {}

        #get element from list
       	word = input_list.pop()
       	print "examining this word %s " % word

        #create dictionary of the element from list 
        for i in range(0, len(word)):
             if word[i] in dictionary_master:
                  dictionary_master[word[i]] += 1
             else:
                  dictionary_master[word[i]] = 1

        print dictionary_master 


        #iterate through other elements in list
        for iterator in input_list:

             #create iterator dictionary 
             dictionary_iterator = {}

             print "examining the iterator %s " % iterator
                     #create dictionary of the element from list
             for j in range(0, len(iterator)):
                 if iterator[j] in dictionary_iterator:
                     dictionary_iterator[iterator[j]] += 1
                 else:
                     dictionary_iterator[iterator[j]] = 1

             print dictionary_iterator
         
             #check if anagrams match
             if dictionary_master == dictionary_iterator:
                  print "FOUND ANAGRAM! %s and %s " % (word, iterator) 





anagram(test_list)
