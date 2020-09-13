def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item==target:
            return index
    return None

if __name__=='__main__':
    user_input = input('Enter numbers separated by comma:\n').strip()
    sequence_ = [int(item) for item in user_input.split(',')]

    target_ = input('Enter a single number to be found in the list: \n')
    target_ = int(target_)
    result = linear_search(sequence_, target_)
    if result is not None:
        print(f'{target_} found at position: {result}')
    else:
        print('Target not found')

'''
------------------------OUTPUT BOX----------------------------------------
Enter numbers separated by comma:
12,13,14,6
Enter a single number to be found in the list: 
6
6 found at position: 3
--------------------------------------------------------------------------
'''