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
# #include<bits/stdc++.h>
# using namespace std;

# int func(vector<vector<int>>&vis, vector<vector<int>>&mat,int i, int j, int m, int n,int len){
#     cout<<i<<j<<endl;
#     if(i>=m || j>=n){
#         return 0;
#     }
#     if(vis[i][j]==1) return 0;
#     if(mat[i][j]==0) return 0;
#     vis[i][j]=1;
#     len+=1;
#     func(vis,mat,i+1,j,m,n,len); //forward
#     func(vis,mat,i,j+1,m,n,len); //downward
#     // func(vis,mat,i+1,j+1,m,n,len); //forward downward
#     // func(vis,mat,i-1,j-1,m,n,len); //backward upward
#     // func(vis,mat,i-1,j+1,m,n,len); //backward downward
#     // func(vis,mat,i+1,j-1,m,n,len); //forward upward
#     // func(vis,mat,i,j-1,m,n,len); //upward
#     // func(vis,mat,i-1,j,m,n,len); //backward
#     return len;
# }
# int main(){
#     vector<vector<int>> mat={{1,1,0,0,0},{0,1,1,0,0},{0,0,1,0,1},{1,0,0,0,1},{0,1,0,1,1}};
#     vector<vector<int>> vis={{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}};;
#     int m=5,n=5;
#     int len=0;
#     // cin>>m>>n;
#     // cout<<"hello"<<endl;
#     // for(int i=0;i<m;i++){
#     //     for(int j=0;j<n;j++){
#     //         cout<<j<<endl;
#     //         vis[i][j]=0;
#     //         // cin>>mat[i][j];
#     //     }
#     // }
#     // cout<<"yess";
#     int ans=func(vis,mat,0,0,m,n,len);
#     cout<<"ans: "<<ans<<endl;
# }
n=int(input())
m=int(input())
mat=[[]]
vis=[[0 for j in range(m)] for i in range(n)]

def isConn(vis,mat,i,j,n,m):
    if i>=n or j>=m:
        return 
    if vis[i][j]
    

