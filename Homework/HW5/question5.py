# Question 5

#
# PERMUTATIONS FUNCTION IS LOCATED BELOW IN FILE!
#

class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, val):
        self.data.append(val)
    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]
    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

class ArrayQueue:
    INITIAL_CAPACITY = 10
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return (self.num_of_elems == 0)
    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1
    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


def permutations(lst):
	
#given a list of integers, return a list containing all the permutations of that list. This function is non-recursive.
    import copy

    numbers_left = ArrayStack()
    answers = ArrayQueue()

    for elem in lst:									#place all numbers into stack
        numbers_left.push(elem)

    while not numbers_left.is_empty():
        if answers.is_empty():								#add in very first number as its permutation
            answers.enqueue([numbers_left.pop()])
        else:
            single = numbers_left.pop()						#isolate one number
            for a in range(len(answers)):					#go through each list block in queue
                permutation = [answers.dequeue()]			#list of list of numbers
                for ind in range(len(permutation)):			#go into list within queue
                    for i in range(len(permutation[ind])+1):		#get index of the list within queue
                        temp = copy.deepcopy(permutation[ind])		#make actual COPY, since insert() changes original
                        temp.insert(i, single)
                        answers.enqueue(temp)						#insert permutation into enqueue
    return answers


s = permutations([1, 2, 3, 4])
print('answers')
while not s.is_empty():
    print(s.dequeue())

