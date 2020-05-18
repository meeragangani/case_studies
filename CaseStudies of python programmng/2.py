tCase=input("Enter Length of array and No. of Queries")
arrlen = tCase.split(" ")

arr=input("Enter Array values: ").split(" ")
arr= [int(i) for i in arr]

que=[]
for i in range(int(arrlen[1])):
    que.append(input("Enter Queries: "))

for i in range(int(arrlen[1])):
    qVal=que[i].split(" ")
    qVal= [int(i) for i in qVal]

    if(qVal[0]==1):
        arr[qVal[1]]=qVal[2] #updation of 1 index by the 2nd
        print(" ")
    elif(qVal[0]==2):
        out=sum(arr[qVal[1]:qVal[2]+1]) #print the arry from 1st index to last index (0:4)
        print(out)