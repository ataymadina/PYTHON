n=int(input("ENTER THE NO OF PAGES : "))
print("ENTER THE PAGE NUMBER: ")
arr =[]
f=[]
for i in range(n):
    arr.append(int(input('')))
no=int(input("ENTER THE NUMBEROF FRAMES : "))
for i in range(no):
    f.append(-1)
h=0
m=0
j=0
for i in range(n):
    print("NO")
    print(arr[i])
    print("\n")
    avail=0
    for k in range(no):
        if(f[k]==arr[i]):
            avail=1
    if(avail==1):
        h=h+1
        print("PAGE FRAME")
        print(f)
    if(avail==0):
        f[j]=arr[i]
        j=(j+1)%no
        m=m+1
        print("PAGE FRAME")
        print(f)
    print("\n")
print("HIT=%d\tMISS=%d"%(h,m))
'''
OUTPUT:
ENTER THE NO OF PAGES : 11
ENTER THE PAGE NUMBER: 
2
3
2
1
5
2
4
5
3
2
5
ENTER THE NUMBEROF FRAMES : 3
NO
2


PAGE FRAME
[2, -1, -1]


NO
3


PAGE FRAME
[2, 3, -1]


NO
2


PAGE FRAME
[2, 3, -1]


NO
1


PAGE FRAME
[2, 3, 1]


NO
5


PAGE FRAME
[5, 3, 1]


NO
2


PAGE FRAME
[5, 2, 1]


NO
4


PAGE FRAME
[5, 2, 4]


NO
5


PAGE FRAME
[5, 2, 4]


NO
3


PAGE FRAME
[3, 2, 4]


NO
2


PAGE FRAME
[3, 2, 4]


NO
5


PAGE FRAME
[3, 5, 4]


HIT=3	MISS=8
'''

