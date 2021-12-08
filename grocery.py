print(
    "Fruits \nNo \t\tItem\t\tAmount/kg \n1 \t\tApple \t\t100 \n2 \t\tWatermelon \t30 \n3 \t\tMuskmelon \t40 \n4  \t\tPeru \t\t30 \n5 \t\tOrange \t\t70"

    "\n\nVegetables \nNo \t\tItem\t\tAmount/kg \n1 \t\tBeans \t\t80 \n2 \t\tBeetroot \t45 \n3 \t\tBrinjal \t40 \n4 \t\tCabbage \t80 \n5 \t\tCarrot \t\t50 \n6 \t\tGinger \t\t240 \n7 \t\tOnion \t\t25 \n8 \t\tTomato \t\t40 \n9 \t\tpotato \t\t20 \n10 \t\tFrenchbean\t85"

    "\n\nBeverages \nNo \t\tItem\t\tAmount/piece \n1 \t\tTropicana \t80 \n2 \t\tReal \t\t45 \n3 \t\tMaaza \t\t80 \n4 \t\tCocacola \t80 \n5 \t\tSprite \t\t80 \n6 \t\tRedbull \t120 \n7 \t\tDuke \t\t40 \n8 \t\tBisleri \t20 \n9 \t\tKinley \t\t20 \n10 \t\tSlice \t\t35"

    "\n\nDairyproducts \nNo \t\tItem\t\tAmount/piece \n1 \t\tMilk \t\t80 \n2 \t\tCurd \t\t80 \n3 \t\tButter \t\t80 \n4 \t\tCheese \t\t200 \n5 \t\tMayo \t\t80 \n6 \t\tMilkpowder \t120 \n7 \t\tDips \t\t40 \n8 \t\tWhey \t\t300 \n9 \t\tIcecream \t200 \n10 \t\tCream \t\t200"

    )

Cart = []
rate = []
total = 0

name = input("Enter you Name: ")
phonenumber = input("Enter you phonenumber: ")
####items####

Beverage = ["Tropicana", "Real", "Maaza", "Cocacola", "Sprite", "Redbull", "Duke", "Bisleri", "Kinley", "Slice"]

Fruits = ["apple", "banana", "Muskmelon", "Watermelon", "Peru", "orange"]

Vegetables = ["Beans", "Beetroot", "Brinjal", "Cabbage", "Carrot", "Ginger", "Onion"]

Dairyproducts = ["milk", "Curd", "Butter", "Cheese", "Mayo", "Milkpowder"]

#####items rate####
Beverage_rate = [90, 80, 50, 80, 70, 120, 30, 20, 25]
dairyproduct_rate = [90, 80, 50, 80, 70, 120, 30]
vegetables_rate = [90, 80, 50, 80, 70, 120, 30]
fruits_rate = [90, 80, 50, 80, 50]


####Beverage####
def beverage():
    c = 0
    for x in Beverage:
        c += 1
        print(f"{c} \t\t{x}")

    P = input("enter your product: ")
    if P == "1" or P == "Tropicana":
        Cart.append(Beverage[0])
        rate.append(Beverage_rate[0])
    if P == "2" or P == "Real":
        Cart.append(Beverage[1])
        rate.append(Beverage_rate[1])
    if P == "3" or P == "Maaza":
        Cart.append(Beverage[2])
        rate.append(Beverage_rate[2])
    if P == "4" or P == "Cocacola":
        Cart.append(Beverage[3])
        rate.append(Beverage_rate[3])
    if P == "5" or P == "Sprite":
        Cart.append(Beverage[4])
        rate.append(Beverage_rate[4])
    if P == "6" or P == "Redbull":
        Cart.append(Beverage[5])
        rate.append(Beverage_rate[5])
    if P == "7" or P == "Duke":
        Cart.append(Beverage[6])
        rate.append(Beverage_rate[6])
    if P == "8" or P == "Bisleri":
        Cart.append(Beverage[7])
        rate.append(Beverage_rate[7])
    if P == "9" or P == "Kinley":
        Cart.append(Beverage[8])
        rate.append(Beverage_rate[8])
    if P == "10" or P == "Slice":
        Cart.append(Beverage[9])
        rate.append(Beverage_rate[9])


#####fruits####
def fruits():
    c = 0
    for x in Fruits:
        c += 1
        print(f"{c} \t\t{x}")

    P = input("enter your product: ")
    if P == "1" or P == "Apple":
        Cart.append(Fruits[0])
        rate.append(fruits_rate[0])
    if P == "2" or P == "Watermelon":
        Cart.append(Fruits[1])
        rate.append(fruits_rate[1])
    if P == "3" or P == "Muskmelon":
        Cart.append(Fruits[2])
        rate.append(fruits_rate[2])
    if P == "4" or P == "Peru":
        Cart.append(Fruits[3])
        rate.append(fruits_rate[3])
    if P == "5" or P == "Orange":
        Cart.append(Fruits[4])
        rate.append(fruits_rate[4])


####vegetables####
def vegetables():
    c = 0
    for x in Vegetables:
        c += 1
        print(f"{c} \t\t{x}")
    P = input("enter your product: ")
    if P == "1" or P == "Beans":
        Cart.append(Vegetables[0])
        rate.append(vegetables_rate[0])
    if P == "2" or P == "Beetroot":
        Cart.append(Vegetables[1])
        rate.append(vegetables_rate[1])
    if P == "3" or P == "Brinjal":
        Cart.append(Vegetables[2])
        rate.append(vegetables_rate[2])
    if P == "4" or P == "Cabbage":
        Cart.append(Vegetables[3])
        rate.append(vegetables_rate[3])
    if P == "5" or P == "Carrot":
        Cart.append(Vegetables[4])
        rate.append(vegetables_rate[4])
    if P == "6" or P == "Ginger":
        Cart.append(Vegetables[5])
        rate.append(vegetables_rate[5])
    if P == "7" or P == "Onion":
        Cart.append(Vegetables[6])
        rate.append(vegetables_rate[6])
    if P == "8" or P == "Tomato" or P == "9" or P == "potato" or P == "10" or P == "Frenchbean":
        print("Not available")


#####Dairy####
def dairyproducts():
    c = 0
    for x in Dairyproducts:
        c += 1
        print(f"{c} \t\t{x}")
    P = input("enter your product: ")
    if P == "1" or P == "Milk":
        Cart.append(Dairyproducts[0])
        rate.append(dairyproduct_rate[0])
    if P == "2" or P == "Curd":
        Cart.append(Dairyproducts[1])
        rate.append(dairyproduct_rate[1])
    if P == "3" or P == "Butter":
        Cart.append(Dairyproducts[2])
        rate.append(dairyproduct_rate[2])
    if P == "4" or P == "Cheese":
        Cart.append(Dairyproducts[3])
        rate.append(dairyproduct_rate[3])
    if P == "5" or P == "Mayo":
        Cart.append(Dairyproducts[4])
        rate.append(dairyproduct_rate[4])
    if P == "6" or P == "Milkpowder":
        Cart.append(Dairyproducts[5])
        rate.append(dairyproduct_rate[5])
    if P == "7" or P == "Dips" or P == "8" or P == "Whey" or P == "9" or P == "Icecream" or P == "10" or P == "Cream":
        print("Not available")


while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to thesupermarket------------------')
    print('a. fruits\nb. vegetables\nc. beverage\nd. Dairyproduct \ne. Exit')
    choice = input('Enter the section of your choice : ')

    if choice == "a" or choice == "Fruits":
        print('------------------fruits------------------')
        fruits()
    elif choice == "b" or choice == "Vegetables":
        print('------------------vegetables------------------')
        vegetables()
    elif choice == "c" or choice == "Beverage":
        print('------------------beverage------------------')
        beverage()
    elif choice == "d" or choice == "Dairyproducts":
        print('------------------dairyproducts------------------')
        dairyproducts()
    elif choice == "e" or choice == "exit":

        print('------------------exited-----------------')
        print(Cart)
        for i in rate:
            total = total + i

        print(f"{name}\t\t{phonenumber}\nyour total bill is {total}")
        print(f"--------------------{name} THANKYOU--------------------")
        break

    else:
        print('You entered an invalid option')
