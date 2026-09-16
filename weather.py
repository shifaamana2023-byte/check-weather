degree=int(input("enter the degree"))
if degree<=20:
    print("cold weather")
elif degree>20 and degree<=38:
    print("normal weather")
else:
    print("hot weather")
fahrenhit=((degree*1.8)+32)
print("the fahrenheit value is ",fahrenhit,"F")
 