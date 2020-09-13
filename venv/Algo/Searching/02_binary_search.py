def binary_search(sorted_collection, item):
    left_index = 0
    right_index = len(sorted_collection)-1
    while left_index <= right_index:
        mid_point = left_index + (right_index-left_index)//2
        current_item = sorted_collection[mid_point]
        if current_item == item:
            return mid_point
        elif item<current_item:
            right_index = mid_point - 1
        else:
            left_index = mid_point + 1
    return None

def __assert_sorted(collection_):
    """
    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True

    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be ascending sorted
    """
    if collection_ != sorted(collection_):
        raise ValueError('Collection must be ascending order')
    return True

if __name__=='__main__':
    import sys
    user_input = input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]

    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be ascending sorted to apply binary search")

    target = input('Enter a single number to be found in the list:\n')
    target_ = int(target)

    result = binary_search(collection, target_)
    if result is not None:
        print(f'{target_} found at position {result}')
    else:
        print(f'{target_} not found in the list')


'''
------------------------OUTPUT BOX----------------------------------------
Enter numbers separated by comma:
12,23,34,45,56
Enter a single number to be found in the list:
23
23 found at position 1
--------------------------------------------------------------------------
'''

'''
------------------------APPENDIX I----------------------------------------
Private Method: '__' is used before any method or function to declare it 
as a private method.
--------------------------------------------------------------------------
'''


