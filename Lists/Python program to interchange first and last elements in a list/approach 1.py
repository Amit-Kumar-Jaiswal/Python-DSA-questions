# Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

def swaplist(newlist):
    size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

newlist = []

a = int(input('Enter the number of list you want to enter : '))
for i in range(a):
    newelements = int(input(f'Enter the number for the element {i} : '))
    newlist.append(newelements)


b = swaplist(newlist)
print(b)