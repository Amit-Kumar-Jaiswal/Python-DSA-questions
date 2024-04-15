#Approach 2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

def swaplist(newlist):
    newlist[0] , newlist[-1] = newlist[-1] , newlist[0]

    return newlist

newlist = []
a = int(input('Enter number of list you want : '))

for i in range(a) :
    new_element = input(f'Enter the number of elements {i} : ')
    newlist.append(new_element)

print(swaplist(newlist))
