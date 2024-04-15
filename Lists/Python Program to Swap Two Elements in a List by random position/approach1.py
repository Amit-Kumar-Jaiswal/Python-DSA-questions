#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

def swaplist(newlist , pos1 , pos2) :

    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp

    return newlist

newlist = []

a = int(input('Enter the number of enlements you want : '))

for i in range(a) :
    new_elements = input(f'Enter the {i} element : ')
    newlist.append(new_elements)

pos1 = int(input('Enter the first element : '))
pos2 = int(input('Enter the second element : '))

print(swaplist(newlist , pos1 , pos2))