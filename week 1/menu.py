def menu():
    print("""
    - MAKANAN -                          - MINUMAN -
    1. SATEY            RM1.00           1. SIRAP            RM3
    2. KEBAB            RM2.00           2. TEH O            RM3
    3. NAAN CHEESE      RM12             3. LIMAU AIS        RM3
    4. ROTI             RM10             4. TEH AIS          RM3
    """)

def orderDetails():
    retry = "y"
    while retry == "y":

        subOrder = []

        item = input("masukkan makanan dan minuman: ")
        totalItem = int(input("quantity: "))
        subOrder.append(item)
        subOrder.append(totalItem)
        order.append(subOrder)

        retry = input("lagi? y/n ")

    else:
        print("ORDER\tQUANTITY")
        for i in range(0,len(order)):
            for j in range(0,len(order)):
                print(order[i][j],end="\t")
        
def totalPrice():
    for i in range(0,len(order)):
        if order[i][0] == "kebab":
            totalPrice = "kebab: RM", order[i][1] * 1
        elif order[i][0] == "naan cheese":
            totalPrice = "naan cheese: RM",order[i][1] * 2
        elif order[i][0] == "satey":
            totalPrice = "satey: RM", order[i][1] * 12
        elif order[i][0] == "roti":
            totalPrice = "roti: RM", order[i][1] * 10
        else:
            print("idk")

    print(totalPrice)
    




answer = "y"
order = []

while answer == "y":
    print("""
            MENU
------------------------------
1 menu makanan dan minuman
2 order details
3 harga
    """)

    choose = input("sila pilih: ")

    if choose == "1":
        menu()
    elif choose == "2":
        orderDetails()
    elif choose == "3":
        totalPrice()
    else:
        print("pilihh betul betul!")

else:
    print("ok")




# 3 fynction wajib
# 1. display makanan and air
# 2. dapatkan details order quantity,type
# 3. display harga