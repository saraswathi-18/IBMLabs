a=[[2,3,4],
   [12,7,5],
   [13,8,10]]
b=[[10,5,3],
   [4,8,15],
   [20,5,14]]
ans=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        ans[i][j]=a[i][j]+b[i][j]

for i in ans:
    print(i)