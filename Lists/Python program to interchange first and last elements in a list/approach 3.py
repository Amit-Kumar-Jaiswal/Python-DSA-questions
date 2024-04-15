

#Approach 3: Swap the first and last element is using tuple variable. 
#Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. 
#Now, the First and last values in that list are swapped. 

def swaplist(newlist) :
    get = newlist[0] , newlist[-1]

    newlist[-1] , newlist[0] = get

    return newlist

newlist = []

a = int(input('Enter the number of elements you want : '))

for i in range(a) :
    newelements = input(f'Enter the number of elements {i} : ')
    newlist.append(newelements)

print(swaplist(newlist))