#Patrick Devine
#Computer Science in Action
#Devin Colwell
#September 15th 2019

def remove(hold):      #This is the function to remove duplicates
    
    print ("The original list is :\n " +  str(hold))

    hold = list(set(hold))      # removes duplicates from given list
    print ("\nThe list after removing duplicates :\n " + str(hold))   


    
    print("\nHere is an indexed list of elements")
    for (num,item) in enumerate(hold):           #enumerate indexes each item in list
        print(num+1,item)


bears = ["Grizzly", "Black", "Black", "teddy", "koala", "koala", "panda","smokey","yogi","yogi",]

remove(bears)   # This is the first list I tested my function on

print("If you would like me to remove duplicates from another list for you\n")  #added option for user to input another list 


input_string = input("Enter a list elements separated by a space \n")    #prompts user for list/takes input
Users_List  = input_string.split()  # Seperated by a space, the elements input by user becomes list held in Users_List variable



remove(Users_List)  #Function is called to remove duplicates and print results
