print('საკონდიტრო მაღაზია "მსუნაგი მოგესსალმებათ"')
name = input(" გთხოვთ მიუთითეთ თქვენი სახელი: ")
print(f'გამარჯობა {name}!')
products = {'brown':9,"bouty":10,"cheescake":11}
print('დღევანდელი პროდუქტების სია: ')
for i in products:
    print(i)
product_name = str(input('მიუთითეთ სასურველი პროდუქტი: ')) # ისედაც სტრინგია ვიცი მაგრამ მაინც დამჭირდა ტერმინალი ცვლადად აღიქვამდა
product_price = products[product_name]
product_count = int(input('გთხოვთ მიუთითოთ რაოდენობა: ')) 
full_price = product_price  *product_count
print(f"გადასახდელი გაქვსთ {full_price} ლარი,")
print('მადლობა რომ ხართ ჩვენი მომხმარებელი')