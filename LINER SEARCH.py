def linearsearch(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return True
    return False

arr=[9, 11, 3, 7 , 8]
key=3
print(linearsearch(arr,key))