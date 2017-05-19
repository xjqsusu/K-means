import math
#initialization
N=eval(input('numbers of points: '))
K=eval(input('numbers of groups: '))
print('choose the method of calculating distance')
print('1 for manhattan')
print('2 for euclidean')
I=eval(input())
#put x-variable in A1 and y-variable in A2
A1,A2=[],[]
for i in range (0,N):
    x=eval(input('input x['+str(i)+']:'))
    y=eval(input('input y['+str(i)+']:'))
    A1.append(x)
    A2.append(y)
#initialize C and C0, which are used to store old and new
#centroid coordinate respectively
C=[[0 for col in range(2)]for row in range(K)]
C0=[[1 for col in range(2)]for row in range(K)]
#chose intial centroids
for i in range (0,K):
    C0[i]=[A1[i],A2[i]]
#when old and new coordinate are not equal, go to while loop.
while (C0!=C):
    
    for i in range (0,K):
        C[i]=C0[i]
#initialize an K x N matrix to store the distance from each point
#to each centroid.
    D=[[0 for col in range(N)]for row in range(K)]    
    for j in range(0,K):
        for i in range (0,N):
            if I==2:
                D[j][i]=math.sqrt((A1[i]-C[j][0])**2+\
                              (A2[i]-C[j][1])**2)
            else:
                D[j][i]=abs(A1[i]-C[j][0])+abs(A2[i]-C[j][1])
#initialize an 1 x N matrix to store the group information,
#ie. G[2]=1 means the second point belongs to group 1.
    G=[1]*N
    for j in range (0,N):
        m=D[0][j]
        for i in range (0,K):
            if D[i][j]<m:
                m=D[i][j]
                G[j]=i+1
#re-calculate the centroid.    
    Count=[0]*K
    SumX,SumY=[0]*K,[0]*K
    for n in range (0,N):
        for x in range (0,K):
            if G[n]==x+1:
                Count[x]+=1
                SumX[x]+=A1[n]
                SumY[x]+=A2[n]
    for i in range (0,K):
        C0[i]=[SumX[i]/Count[i],SumY[i]/Count[i]]
#print result.
if I==1:
    print('this program is using Manhattan distance')
else:
    print('this program is using Euclidean distance')
for i in range (0,N):
    print('('+str(A1[i])+','+str(A2[i])+') belongs to group'\
          +str(G[i]))


