def occurance(t) :

    occu={}

    for i in t:
        if i in occu:
            occu[i]=occu[i]+1
        else:
            occu[i]=1
    return occu
    


t=(1,2,3,3,1,4,5,6,5)

print(occurance(t))