def circle():
    radius = int(input("enter radius: "))
    result = (22/7)*radius

    print("area of circle is ",result,"cm")

def triangle():
    tapak = int(input("enter tapak: "))
    tinggi = int(input("enter tinggi: "))

    result = (1/2) * tapak * tinggi

    print("area of triangle is ",result,"cm")

def square():
    panjang = int(input("enter panjang: "))
    lebar = int(input("enter lebar: "))

    result = panjang * lebar

    print("area of square is ",result,"cm")

def trapezium():
    tapak1 = int(input("enter tapak A: "))
    tapak2 = int(input("enter tapak B: "))
    tinggi = int(input("enter tinggi: "))

    result = (1/2)*(tapak1+tapak2)*tinggi

    print("area of trapezium is ",result,"cm")



