# Filename:  list_manipulator.py
def manipulate_list(data):
    #remove duplicates, sort, return
    unique_data = list(set(data))
    unique_data.sort()
    return unique_data

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
manipulated_list = manipulate_list(my_list)
print(manipulated_list) # Output: [1, 2, 3, 4, 5, 6, 9]