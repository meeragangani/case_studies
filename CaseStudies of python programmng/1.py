tcase=int(input("Enter the no of test case:"))

for i in range(tcase):
    str1=(input("Enter String 1 for test case "+str(i+1)+ ": ")).lower()
    str2=(input("Enter String 2 for test case "+str(i+1)+ ": ")).lower()

    chars1=[0]*26;chars2=[0]*26

    #find out the frequency
    for i in range(len(str1)-1):
        chars1[ord(str1[i])-97]+=1

    for i in range(len(str2)-1):
        chars2[ord(str2[i])-97]+=1

    count=0
    for i in range(26):
        count=count+abs(chars1[i]-chars2[i])

    print(count)