year = int(input("Please Enter the Year Number you wish: "))
 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is yes" %year)
else:
    print("%d is no" %year)
    
