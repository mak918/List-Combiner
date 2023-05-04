

def combine_list_files():
    """Combine two text files of lists separated by a comma and space."""
    input1_name, input2_name, output_name = read_config_file()

    input1_list = get_input_list(input1_name)
    input2_list = get_input_list(input2_name)

    output_list = combine_lists(input1_list, input2_list)

    write_list_to_file(output_list, output_name)


def read_config_file():
    """Get the names of the input files and output file from the config file."""
    with open("config.txt", 'r') as config_file:
        input1_name = config_file.readline().rstrip().split()[3]
        input2_name = config_file.readline().rstrip().split()[3]
        output_name = config_file.readline().rstrip().split()[2]
    return [input1_name, input2_name, output_name]


def get_input_list(input_file):
    """Get an input list from a specified input file."""
    with open(input_file, 'r') as input_string:
        input_string = input_string.read().rstrip()
    # turn the input from a string into a list
    input_list = input_string.split(', ')
    return input_list


def combine_lists(list1, list2):
    """Combine two given lists into a single list.

    The resulting combined list will be sorted,
    and any repeat elements (coming from both lists)
    will be removed. Repeat elements within the same
    list will persist.
    """
    # sort the lists to find duplicate items easier
    list1 = sorted(list1, key=str.lower)
    list2 = sorted(list2, key=str.lower)

    iter1, iter2 = 0, 0  # set up variables to keep track of position within each list
    list_final = []  # prepare a space for the final list

    while iter1 < len(list1) and iter2 < len(list2):       # while each list still has items to process
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

    return list_final


# turn the final list into a string, with each item separated by a comma and space
def write_list_to_file(list_to_write, file_name):
    """Turn a list into a string before writing it to a specified file."""
    # convert the list to a string of elements separated by commas
    list_string = ', '.join(list_to_write)

    # write the string to the specified file
    with open(file_name, 'w') as output:
        output.write(list_string)


if __name__ == "__main__":
    combine_list_files()
