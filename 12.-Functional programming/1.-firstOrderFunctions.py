a1 = [5,4,3,2,1]
a2 = [1,2,3,4,5]
a3 = [3,2,1]

def compare(arr1,arr2,func):
    return [func(val1,arr2[idx]) for idx, val1 in enumerate(arr1)]

def greater(val1, val2):
    return val1 > val2

def minor(val1,val2):
    return val1 < val2

print(compare(a1,a2,greater))
print(compare(a1,a2,minor))
#print(compare(a1,a3,greater))

'''
def verifyLength(func):
    def new(arr1,arr2,callback):
        if not len(arr1) == len(arr2):
            print("I can't do it!")
        else: 
            return func(arr1,arr2,callback)
    return new

@verifyLength
def compare(arr1,arr2,func):
    return [func(val1,arr2[idx]) for idx, val1 in enumerate(arr1)]

print(compare(a1,a2,greater))
print(compare(a1,a2,minor))
print(compare(a1,a3,greater))
'''