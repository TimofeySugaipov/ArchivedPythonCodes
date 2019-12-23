# Candidate number: 14459
# Using Python 3

# Test if a list A of integers is sum free
# Your code should co here
def isSumFree(L):
    for x in range(len(L)):
        A = [n for n in L]
        sums = []
        A.pop(x)
        for i in range(len(A)):
            for value in A[i+1:]:
                S  = A[i]+value
                if S not in sums:
                    sums.append(S)
        if L[x] in sums:
            return False
    return True
    
if __name__ == '__main__':

    # Test if a list A of increasing integers between 1 and 10 is sum free    
    # Your code should go here
    for a in range(1,7):
        for b in range(a+1,8):
            for c in range(b+1,9):
                for d in range(c+1,10):
                    for e in range(d+1,11):
                        L = [a,b,c,d,e]
                        if isSumFree(L):
                            print(*L)
