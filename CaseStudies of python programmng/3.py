#zoooooo
a = input("Enter the string")
x=0
y=0
for i in range(len(a)):
    if a[i] == 'z':
        x += 1
    else:
        if a[i] == 'o':
            y += 1
if x*2==y:
    print("Yes")
else:
     print("No")
