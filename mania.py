def amouter(pricePerUnit, amoutAll):
    notDiscount = float(pricePerUnit) * int(amoutAll)
    return round(notDiscount, 2)

def discouter(price):
    if price >= 10000:
        discout = price*10/100
    elif price >= 3000:
        discout = price*5/100
    else:
        discout = 0
    return discout

goodsDict = {
    1: {"name": "pc", "price": 34990},
    2: {"name": "laptop", "price": 23990},
    3: {"name": "smartphone", "price": 9990},
    4: {"name": "printer", "price": 3490},
    5: {"name": "tablet", "price": 10900}
}

print("\n***ยินดีต้อนรับเข้าสู่ร้าน TechNo Shopping***")
for idx, product in goodsDict.items():
    print("{} = {} บาท".format(product["name"], product["price"]))
print("*************************************")

selectMenu = int(input("กรุณาพิมพ์รายการที่ต้องการขาย (หมายเลข): "))
amountSelected = int(input("กรุณาใส่จำนวนสินค้าที่ซื้อ: "))
print("*************************************")

if selectMenu in goodsDict:
    selectedProduct = goodsDict[selectMenu]
    pricePerUnit = selectedProduct["price"]
    price = amouter(pricePerUnit, amountSelected)
    discount = discouter(price)
    summary = price - discount
    print("\n***********สรุปรายการคำสั่งซื้อ***********")
    print(f"สินค้าที่ซื้อ: {selectedProduct['name']}, {pricePerUnit} x {amountSelected}\nราคาก่อนได้รับส่วนลด: {price} บาท\nส่วนลดในการซื้อ: {round(discount, 2)} บาท\nราคาที่ต้องชำระ: {summary} บาท")
    print("*************************************")
else:
    print("โปรแกรมหยุดการทำงาน!! ไม่พบรายการที่คุณป้อนเข้าไป ¯\_(ツ)_/¯")

print("นายรวิพล วนะภูติ 6611505741")