# Combine two text files of lists separated by a comma and space

# get the names of the input files, and output file from the config file
with open("config.txt", 'r') as config_file:
    input1_name = config_file.readline().rstrip().split()[3]
    input2_name = config_file.readline().rstrip().split()[3]
    output_name = config_file.readline().rstrip().split()[2]

# get the input lists from the specified input files
with open(input1_name, 'r') as input1, open(input2_name, 'r') as input2:
    list1 = input1.read().rstrip()
    list2 = input2.read().rstrip()

# turn the inputs from strings to lists
list1 = list1.split(', ')
list2 = list2.split(', ')

# sort the lists to find duplicate items easier
list1 = sorted(list1, key=str.lower)
list2 = sorted(list2, key=str.lower)

iter1, iter2 = 0, 0  # set up variables to keep track of position within each list
list_final = []  # prepare a space for the final list

while iter1 < len(list1) and iter2 < len(list2):  # while each list still has items to process
    if list1[iter1].lower() == list2[iter2].lower():   # if both input lists have the same item,
        list_final.append(list1[iter1])                # insert it in the final list once,
        iter1 += 1                                     # and advance each input list
        iter2 += 1
    elif list1[iter1].lower() < list2[iter2].lower():  # if the item in the first input list comes before
        list_final.append(list1[iter1])                # the second alphabetically, add the item from the first list
        iter1 += 1                                     # and advance the first list
    else:
        list_final.append(list2[iter2])                # otherwise add the item from the second input list
        iter2 += 1                                     # and advance the second list

# at this point one of the input lists has gone through every item
if iter1 >= len(list1):                  # if the first list has been completed
    while iter2 < len(list2):            # go through the remainder of the second list
        list_final.append(list2[iter2])  # and add each item into the final list
        iter2 += 1                       # and advance the second list
else:
    while iter1 < len(list1):            # otherwise, it must be the second list that was completed, so go through
        list_final.append(list1[iter1])  # the first list, adding each item to the final list
        iter1 += 1                       # and advance the first list

# turn the final list into a string, with each item separated by a comma and space
list_final_string = ', '.join(list_final)

# write the output string to the specified output file
with open(output_name, 'w') as output:
    output.write(list_final_string)
