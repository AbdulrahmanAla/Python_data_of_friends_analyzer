#############################################################################
# Project 8
#
# create an open_file function that prompts the user to input a file name to open and keeps prompting until a correct name is entered
#
# create read name function that reads the Names.txt file using file pointer fp and return list of names
#
# create_friends_dict function, that takes the two lists created in the read_names function and the read_friends function and builds a dictionary. Build a dictionary with name as the key and a list of friends as the value.
#
#This function takes two names and the friends_dict and returns a set of friends that the two names have in common.
#
# create find_max_friends function, This function takes a list of names and the corresponding list of friends and determines who has the most friends (max_number).
#
# create find_max_common_friends function, This function takes two names and the friends_dict and returns a set of friends that take the two names have in common. 
#
# create find_second_friends, the pourpose of this function is to get the second-order friendships, that is, friends of friends. For each person in the network find the friends of their friends, without including the person or their friends.
#
# create find_Max_second_friends function, Here we again consider second-order friendships, that is, friends of friends.  similar to finding max friends you will find max second-order friends.
#
# create a menue where a user enters an option between 1 and 5 that correspond to each command
#
#############################################################################
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''

#This function prompts the user to input a file name to open and keeps prompting until a correct name is entered
def open_file(s):
    '''Docstring'''
    loop= True
    while loop == True: # here I made a loop so the user will be asked many times until they enter a valid file name
        try:
            promot= input("\nInput a {} file: ".format(s))
            filename= promot
            fp= open(filename,"r")# opened the file in reading mode
            loop = False
        except FileNotFoundError:# I made an except if the file wasn't found an error message wil be printed and the user will be asked again
            print("\nError in opening file.")
    
    return fp

#This function reads the Names.txt file using file pointer fp and return list of names
def read_names(fp):
    '''Docstring'''
    names_list= [] # here I created a list to add the names on it later on.
    for line in fp: 
        line= line.strip() # here I made a strip to the line as asked in the document.
        names_list.append(line) #here I added the line in the list.

    return names_list

#This function reads the Friends.csv file using file pointer, fp.
def read_friends(fp,names_lst):
    '''Docstring'''
    list_of_friends=[] # here I created a list to add the names on it later on.
    for line in fp:
        line1= line.strip() # here I made the strip method to delete the \n at the end of every line.
        line1= line1.strip(",")#  striped the comma at the end of every line
        loop_list= line1.split(",")#  converted the line to a list of the values, separated by commas.
        list_= [] 
        for i in loop_list:
            list_.append(names_lst[int(i)])# to match the index to the name list
        list_of_friends.append(list_)# append the value to the list of friends
    return list_of_friends

#This function takes the two lists created in the read_names function and the read_friends function and builds a dictionary. Build a dictionary with name as the key and a list of friends as the value.
def create_friends_dict(names_lst,friends_lst):
    friends_dict= dict(zip(names_lst,friends_lst))# here I created dicotanry and used zip method to link each first iteam of both lists
    return friends_dict
    
#This function takes two names and the friends_dict and returns a set of friends that the two names have in common.           
def find_common_friends(name1, name2, friends_dict):
    name1_value= friends_dict[name1]# this line get friends of name 1
    name2_value= friends_dict[name2]# this line get friends of name 2
    set_of_friends= set()#create a set
    
    for i in name1_value: # take the friends of the first name
        if i in name2_value:# check if the friend of the first name is in the friends of the second name
            set_of_friends.add(i)# it would add the friend name if the friend of the first name is in the friends of the second name
        
    return set_of_friends 
    

    
#This function takes a list of names and the corresponding list of friends and determines who has the most friends (max_number).
def find_max_friends(names_lst, friends_lst):
    '''Docstring'''
    list_of_number_of_friends=[] # create a list to know the  number of friends
    for i in friends_lst:# loop in the friends list
        list_of_number_of_friends.append(len(i)) # check the number of friends the name have and append it inside the list_of_number_of_friends
    max_number= max(list_of_number_of_friends) # get the max number from the list
    indexes=[] # here I made a temprory list 
    max_number_for_friends=[]# get the max number of friends
    for i,char in enumerate(friends_lst): #loop on the original list to get the index of the max number of friends
        if len(char) == max_number:
            indexes.append(i)# append the index if the max number is the same as lentgh of the character
    for i in indexes:# loop on the indexes to get the names 

        max_number_for_friends.append(names_lst[i])# apend the name from the name list
    max_number_for_friends= sorted(max_number_for_friends)# sort the listas asked in the pdf
    return max_number_for_friends,max_number 



#This function takes two names and the friends_dict and returns a set of friends that take the two names have in common. 
def find_max_common_friends(friends_dict):
    '''Docstring'''
    common_friends_dic= {} #
    names_list = []
    for i in friends_dict:# get the first name in the friends dictionary
        for p in (friends_dict): # get the Second name in the friends dictionary
            if i == p: # it would skip the case if the first name is same as the second one
                continue
            tup=(i,p) # create a tuple with the first name and the second one
            common_friends_value= find_common_friends(i,p,friends_dict)# get the common friends of the two names
            common_friends_dic[tup]= common_friends_value# add the previous value to the dictonary
    maximum_common = []
    for max_value in common_friends_dic.values():
        maximum_common.append(len(max_value))
    max_commn_friends_value= max(maximum_common)# find the max common friends value
    max_commn_friends_value= max_commn_friends_value# get the lenthg of the list of the max commn friends
    max_friends = []
    for names,count in common_friends_dic.items(): # loop to the commn friend dic
        if len(count) == max_commn_friends_value and names[0] not in names_list and names[1] not in names_list: # get the names insde a list and make these conditions so the names wouldn't duplicate with different indexes
            names_list.append(names[0])
            names_list.append(names[1])
            max_friends.append(names)# append it to the list
    return sorted(max_friends),max_commn_friends_value # sort the list as indicated in the document


#the pourpose of this function is to get the second-order friendships, that is, friends of friends. For each person in the network find the friends of their friends, without including the person or their friends   
def find_second_friends(friends_dict):
    '''Docstring'''
    friends_of_name=[]
    dic = {}
    for person_name,friends in friends_dict.items():
        friends_set = set()
        friends_of_friends = set()
        for value in friends:
            friends_set.add(value)
            for a_name in friends_dict[value]:
                friends_of_friends.add(a_name)
        dic[person_name] = friends_of_friends-friends_set-{person_name}
    return dic



#Here we again consider second-order friendships, that is, friends of friends.  similar to finding max friends you will find max second-order friends.
def find_max_second_friends(seconds_dict):
    maximum_list = []
    maximum_names = []
    for count in seconds_dict.values(): # this line would get the values in second_dict 
        num = len(count) # get the lentgh of the variable count
        maximum_list.append(num)# append it to the maximum_list
    max_num = max(maximum_list)# this line would give us the maximum value in the maximum list
    for key,value in seconds_dict.items(): # this line would give us both the keys and the values of the second dict
        if max_num == len(value): # this line would check if the value is a maximum value or not
            maximum_names.append(key) # if it was equal to the max value it would get appended
    return maximum_names,max_num

def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4": # this choice would ask the user a promot for a name and check if the name is on the name list or not and if a name is not in the  list it would produce an error message
            prompt_name = input("\nEnter a name: ")
            while prompt_name not in names_lst:# check if the promot is in the list
                print("\nThe name {} is not in the list.".format(prompt_name))
                prompt_name = input("\nEnter a name: ")# promot for a file name
            print("\nFriends of {}:".format(prompt_name))
            for names in friends_dict[prompt_name]:
                print(names)

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
