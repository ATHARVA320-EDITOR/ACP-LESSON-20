def SquaredValues(beg, end):

    lst = []
    for i in range(beg, end+1):
        lst.append(i**2)
    lst_even = []
    lst_odd = []
    for i in lst:
        if i%2==0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    print("Here is a list of even squares within specified ranges: ",lst_even)
    print("Here is a list of odd squares within specified ranges: ",lst_odd)
    
beg = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
print(SquaredValues(beg,end))
    