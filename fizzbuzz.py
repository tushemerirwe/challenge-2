def fizzbuzz(list1, list2):
    totallist = list1+list2
    i = len(totallist)
    
    if i % 3 ==0 and i % 5 == 0:
        return "fizzbuzz" 

    elif i % 3 == 0:
        return "fizz"
    elif  i % 5 == 0:
        return "buzz" 
    else:
        return i


print(fizzbuzz([1,2,3,4,5,6],[7,1,6,5]))
            


    
    
