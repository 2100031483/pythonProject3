import math
print("1-circle    2-rectangle    3-triangle")
side =input("select no of sides: " )
if side=='1':
    print("for circle: ")
    from math import pi
    a=int(input("a= "))
    area=(pi*a*a)
    print("area= ")
    print(float(area))
    peri=(2*pi*a)
    print("peri= ")
    print(float(peri))
elif side=='2':
    print("for rectangle:")
    l=int(input("l= "))
    b=int(input("b= "))
    rec_area=(l*b)
    print("area=",rec_area)
    rec_peri=(2*(l+b))
    print("peri=",rec_peri)
elif side == '3':
    print("for triangle:")
    s1 = int(input("side1= "))
    s2 = int(input("side2= "))
    s3 = int(input("side3= "))
    p=(s1+s2+s3)/2
    from math import sqrt
    tri_area=sqrt(p*(p-s1)*(p-s2)*(p-s3))
    print("area=",tri_area)
    tri_peri=(s1+s2+s3)
    print("peri=",tri_peri)
else :
    print("invalid choice")
