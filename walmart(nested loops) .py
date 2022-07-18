fruit=["apple","litchi","cherry","peru  ","kiwi  ",]
fprice=[100,30,40,30,70,]
veg=["beans  ","beet   ","brinjal","cabbage","carrot ","ginger","onion  "]
vprice=[80,45,40,80,50,240,25,]
bev=["real    ","mazza   ","cocacola","sprite  ","redbull ","duke    ","slice   ",]
bprice=[40,40,50,50,120,250,40,]
final=[]
finalp=[]
sum=0
def menu():
   print("Fruits")
   print("no"+"         "+"Item"+"          "+"Amount/kg")
   for i in range(len(fruit)-1):
       print(str(i+1)+"          "+fruit[i]+"          "+str(fprice[i]))

   print("Vegetables")
   print("no" + "         " + "Item" + "          " + "Amount/kg")
   for i in range(len(veg)-1):
       print(str(i + 1) + "          " + veg[i] + "         " + str(vprice[i]))

   print("Beverages")
   print("no" + "         " + "Item" + "          " + "Amount/kg")
   for i in range(len(bev)-1):
       print(str(i + 1) + "          " + bev[i] + "        " + str(bprice[i]))
def fru():
   print("Fruits")
   print("no" + "         " + "Item" + "          " + "Amount/kg")
   for i in range(len(fruit)):
       print(str(i + 1) + "          " + fruit[i] + "          " + str(fprice[i]))
   while True:
       ch1=input("enter your product or press 0 to exit ")
       if(ch1 == "apple" or ch1 == "1"):
           final.append(fruit[0])
           finalp.append(fprice[0])
       elif(ch1=="litchi" or ch1=="2"):
           final.append(fruit[1])
           finalp.append(fprice[1])
       elif (ch1 == "cherry" or ch1 == "3"):
           final.append(fruit[2])
           finalp.append(fprice[2])
       elif (ch1 == "peru" or ch1 == "4"):
           final.append(fruit[3])
           finalp.append(fprice[3])
       elif (ch1 == "kiwi" or ch1 == "5"):
           final.append(fruit[4])
           finalp.append(fprice[4])
       elif(ch1=="exit" or ch1=="0"):
           break
       else:
           print("enter valid entity")

def vege():
   print("Vegetables")
   print("no" + "         " + "Item" + "          " + "Amount/kg")
   for i in range(len(veg)):
       print(str(i + 1) + "          " + veg[i] + "         " + str(vprice[i]))
   while True:
       ch2=input("enter your product or press/type 0 to exit ")
       if (ch2 == "beans" or ch2 == "1"):
           final.append(veg[0])
           finalp.append(vprice[0])
       elif (ch2 == "beet" or ch2 == "2"):
           final.append(veg[1])
           finalp.append(vprice[1])
       elif (ch2 == "brinjal" or ch2 == "3"):
           final.append(veg[2])
           finalp.append(vprice[2])
       elif (ch2 == "cabbage" or ch2 == "4"):
           final.append(veg[3])
           finalp.append(vprice[3])
       elif (ch2 == "carrot" or ch2 == "5"):
           final.append(veg[4])
           finalp.append(vprice[4])
       elif (ch2 == "ginger" or ch2 == "6"):
           final.append(veg[5])
           finalp.append(vprice[5])
       elif (ch2 == "onion" or ch2 == "7"):
           final.append(veg[6])
           finalp.append(vprice[6])
       elif (ch2 == "exit" or ch2 == "0"):
           break
       else:
           print("enter valid entity")

def beve():
   print("Beverages")
   print("no" + "         " + "Item" + "          " + "Amount/kg")
   for i in range(len(bev)):
       print(str(i + 1) + "          " + bev[i] + "        " + str(bprice[i]))
   while True:
           ch3=input("enter your product or press/type 0 to exit")
           if (ch3 == "real" or ch3 == "1"):
               final.append(bev[0])
               finalp.append(bprice[0])
           elif (ch3 == "mazza" or ch3 == "2"):
               final.append(bev[1])
               finalp.append(bprice[1])
           elif (ch3 == "cocacola" or ch3 == "3"):
               final.append(bev[2])
               finalp.append(bprice[2])
           elif (ch3 == "sprite" or ch3 == "4"):
               final.append(bev[3])
               finalp.append(bprice[3])
           elif (ch3 == "redbull" or ch3 == "5"):
               final.append(bev[4])
               finalp.append(bprice[4])
           elif (ch3 == "duke" or ch3 == "6"):
               final.append(bev[5])
               finalp.append(bprice[5])
           elif (ch3 == "slice" or ch3 == "7"):
               final.append(bev[6])
               finalp.append(bprice[6])
           elif (ch3 == "exit" or ch3 == "0"):
               break
           else:
               print("enter valid entity")

menu()
n=input("enter your name ")
no=int(input("enter your phone no. "))
while True:
   print("\n")
   print("---------------------Welcome To The Supermarket---------------------")
   print("a.fruits \nb.vegetables \nc.beverages \nd.exit (billing process)")
   user=input("Enter your choice of selection: ")
   if(user=="fruits" or user=="a"):
     fru()
   elif(user=="vegetables" or user=="b"):
     vege()
   elif(user=="beverages" or user=="c"):
     beve()
   elif(user=="exit" or user=="d"):
     break
   else:
     print("enter valid entity")
     continue

print("\n-------------bill-------------")
print("Name : "+n)
print("phone : "+str(no))
for j in range(len(final)):
   print(str(j+1)+"        "+final[j])
   sum+=finalp[j]
print("\nTotal bill is : "+str(sum))
print("THANKS FOR SHOPPING \nPLEASE VISIT AGAIN")
