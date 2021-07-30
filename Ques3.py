def countMin(str, i, l):
    if (i == l):
        return 0
    if (i == l - 1):
        return 0 if(str[i] == str[l]) else 1
 
    if(str[i] == str[l]):
        return countMin(str, i + 1, l - 1)
    else:
        return (min(countMin(str, i, l - 1),
                    countMin(str, i + 1, l)) + 1)
 
     
str = "wodsw"
print(countMin(str, 0, len(str) - 1))