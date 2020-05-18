def switch_func():
    t=int(input("Enter the number that you want"))
    while t > 0:
        n=int(input("Enter the Seat number"))
        rem=n%12
        if rem==0:
            print(n-11,"Window Seat")
        elif rem==1:#1%12=1+11
            print(n+11,"Window Seat")
        elif rem==2:#2%12=2+9=11
            print(n+9,"Aisle Seat")
        elif rem==3:#3%12=3+7=10
            print(n+7,"Aisle Seat")
        elif  rem==4:#4%12=4+5=9
            print(n+5,"Aisle Seat")
        elif rem==5:#5%12=5+3=8
            print(n+3,"Middle Seat")
        elif rem==6:# 6%12=6+1=7
            print(n+1,"Window Seat")
        elif rem==7:#7%12=7-1
            print(n-1,"Window Seat")
        elif rem==8:
            print(n-3,"Middle Seat")
        elif rem==9:
            print(n-5,"Aisle Seat")
        elif rem==10:
            print(n-7,"Aisle Seat")
        elif rem==11:
            print(n-9,"Middle Seat")
        else:
            print("Nothing")

print('The result for inp is : ', switch_func())

