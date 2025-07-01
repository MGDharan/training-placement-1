# Filename:  tuple_manipulation.py
def tuple_operations(my_tuple):
    """Performs various operations on a tuple."""
    print("Original tuple:",my_tuple)
    print("Length of tuple:",len(my_tuple))
    print("Tuple after adding an element:",my_tuple + (10,))
    print("Sliced tuple:",my_tuple[1:4])
    print("Max value in tuple:",max(my_tuple))