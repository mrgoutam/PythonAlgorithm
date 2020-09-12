# using dictionaries to construct graph
class AdjacentList:
    def __init__(self):
        self.list_ = {}

    def addEdge(self, from_vertex, to_vertex):

        # checking if vertex is already present in the dictionary
        # if present, get the list by the key (from_vertex)
        # append to_vertex to that list
        # and then update the dictionary
        if from_vertex in self.list_.keys():
            vertex_list = self.list_[from_vertex]
            vertex_list.append(to_vertex)
            self.list_[from_vertex] = vertex_list

            # or
            # self.list_[from_vertex].append(to_vertex)
        else:
            self.list_[from_vertex] = [to_vertex]

    def printGraph(self):
        print('Dictionary: ')
        print(self.list_,'\n')

        print('Adjacent List: ')
        for i in self.list_:
            print((i, "->", " -> ".join([str(j) for j in self.list_[i]])))

if __name__== '__main__':
    al = AdjacentList()
    al.addEdge(0, 1)
    al.addEdge(0, 4)
    al.addEdge(4, 1)
    al.addEdge(4, 3)
    al.addEdge(1, 0)
    al.addEdge(1, 4)
    al.addEdge(1, 3)
    al.addEdge(1, 2)
    al.addEdge(2, 3)
    al.addEdge(3, 4)

    al.printGraph()

'''
------------------------OUTPUT BOX----------------------------------------
Dictionary: 
{0: [1, 4], 4: [1, 3], 1: [0, 4, 3, 2], 2: [3], 3: [4]} 

Adjacent List: 
(0, '->', '1 -> 4')
(4, '->', '1 -> 3')
(1, '->', '0 -> 4 -> 3 -> 2')
(2, '->', '3')
(3, '->', '4')
--------------------------------------------------------------------------
'''

'''
------------------------APPENDIX I----------------------------------------
What is join?
The join() method is a string method and returns a string in which the 
elements of sequence have been joined by str separator.
Syntax: string_name.join(iterable)
--------------------------------------------------------------------------
'''
print('\n')
print('APPENDIX I:')
dummy_list = ['1', '2', '3', '4']
str_to_be_append = " -> "
result_str = str_to_be_append.join(dummy_list)
print(result_str)

'''
------------------------OUTPUT BOX----------------------------------------
APPENDIX I:
1 -> 2 -> 3 -> 4
--------------------------------------------------------------------------
'''