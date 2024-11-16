price=int(input("enter price"))
if price>50:
    print("price-price*0.1")
elif 20<=price<=50:
    print("price-price*0.05")
elif price<20:
    print("no discount")
