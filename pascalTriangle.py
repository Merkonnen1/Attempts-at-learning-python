ListOdd = []
ListEven = []
s = 0
def pascalTriangle(n):
    q = 1
    if n == 1:
        return(ListOdd)
    while q != n:
        if q % 2 != 0:
            if q != 1:
                ListEven.clear()
                for w in range(len(ListOdd)-1):
                    ListEven.append(ListOdd[w] + ListOdd[w + 1])
            ListEven.append(1)
            ListEven.insert(0,1)
        else:
            ListOdd.clear()
            for w in range(len(ListEven)-1):
                ListOdd.append(ListEven[w] + ListEven[w + 1])
            ListOdd.append(1)
            ListOdd.insert(0, 1)
        q += 1
    if len(ListOdd)<=len(ListEven):
        return(ListEven)
    else:
        return(ListOdd)

# some random comment for git purposes
print(pascalTriangle(int(input("What is your number?: "))))