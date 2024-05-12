
# class to implement unordered list 
class UnorderedList:
    """ This is a class implementation of Unordered List """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

my_list = [1, 2, 3, 4]
big_list = [my_list] * 3
print(big_list)
my_list[2] = 45
del my_list[2]
print(big_list)