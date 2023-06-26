# Backtracking problems
# 1. Generate all the binary strings with n bits. Assume[0..n-1] is an array of size n.
def generate_binary_strings(ans,str,n):
    if n == 0:
        ans.append(str)
        return
    generate_binary_strings(ans,str+'0',n-1)
    generate_binary_strings(ans,str+'1',n-1)

ans=[]
str=""
n=int(input())
generate_binary_strings(ans,str,n)
print(ans)

# 2. Find the length of connected cells of 1s in a matrix of 0s and 1s
n=int(input())
m=int(input())
mat=[[]]
vis=[[0 for j in range(m)] for i in range(n)]

def isConn(vis,mat,i,j,n,m):
    

