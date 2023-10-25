def binary_search_algo(a,s):
    low=0
    high=len(a)-1
    print(a)
    while(low <= high ):
        mid=(low+high)//2
        if(s == a[mid]):
            return mid
            break
        elif(s<=a[mid]):
            high=mid-1
            low=low
        else:
            low=mid+1
            high=high
    else:
        return "Element Not FOund"
    
a=[7,3,4,5,1,2,9]
a.sort()
s=int(input("enter search"))

print(binary_search_algo(a,s))

