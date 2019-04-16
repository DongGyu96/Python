import random
lst = [30, 1, 2, 1, 0]
print("lst : ", lst)

lst.append(40)
print("lst.append(40) : ", lst)

lst = [30, 1, 2, 1, 0]
lst.insert(1, 43)
print("lst.insert(1, 43) : ", lst)

lst = [30, 1, 2, 1, 0]
lst.extend([1, 43])
print("lst.extend([1,43]) : ", lst)

lst = [30, 1, 2, 1, 0]
lst.pop(1)
print("lst.pop(1) : ", lst)

lst = [30, 1, 2, 1, 0]
lst.pop()
print("lst.pop() : ", lst)

lst = [30, 1, 2, 1, 0]
lst.reverse()
print("lst.reverse : ", lst)

lst = [30, 1, 2, 1, 0]
random.shuffle(lst)
print("lst.random.shuffle(lst) : ", lst)
