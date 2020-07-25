import collections

"""
Python Maps also called ChainMap is a type of data structure to manage 
multiple dictionaries together as one unit. The combined dictionary contains 
the key and value pairs in a specific sequence eliminating any duplicate keys. 
The best use of ChainMap is to search through multiple dictionaries at a time and 
get the proper key-value pair mapping. We also see that these ChainMaps behave as 
stack data structure.
"""
# Creating a chain map
def createChainMap():
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    # order of insertion of dictionary matters
    res = collections.ChainMap(dict1, dict2)

    # Creating a single dictionary
    print(res.maps, '\n')

    print('Keys = {}'.format(list(res.keys())))
    print('Values = {}'.format(list(res.values())))
    print()

    # Print all the elements from the result
    print('elements:')
    for key, val in res.items():
        print('{} = {}'.format(key, val))

    # Find a specific value in the result
    print('day3 in res: {}'.format(('day1' in res)))
    print('day4 in res: {}'.format(('day4' in res)))
createChainMap()

print("----------------Update Map-----------------")
"""
When the element of the dictionary is updated, the result is instantly updated in the result 
of the ChainMap. In the below example we see that the new updated value reflects in the result 
without explicitly applying the ChainMap method again
"""

def updateMap():
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day4': 'Thu'}

    res = collections.ChainMap(dict1, dict2)
    print(res.maps, '\n')
    dict2['day4'] = 'Fri'
    print(res.maps, '\n')
updateMap()