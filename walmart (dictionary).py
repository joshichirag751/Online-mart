shops={"vegetables" :
           {"carrot": 40 ,
            "cabbage": 50,
            "cucumber" : 25},
       "clothes" :
           {"pant" : 200,
            "shirt" : 150,
            "tshirt" : 200},
       "footwear" :
           {"slippers" : 100,
            "shoes" : 500,
            "heels" : 300}
       }
bought=[]
bill=[]
while True:
    print("What do you want to buy?")
    for x in shops:
        print (x)
    option= input()
    if option == "exit":
        break
    else:
        for x in shops:
            if x == option:
                print("Which", x, "do you want to buy?", (shops[x]))
                a=input()
                y=input(f"Are you sure you want to buy  {a} ?")
                if y=="yes":
                    bought.append(a)
        for i,j in shops.items():
            for key in j:
                if key == a:
                    print (j[key])
                    bill.append(j[key])


print (bought)
print(bill)