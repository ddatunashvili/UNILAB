# -*- coding: utf-8 -*-
class shop_game():
    
    def __init__(self):
        print('საკონდიტრო მაღაზია "მსუნაგი მოგესალმებათ')
        self.name = input(" გთხოვთ მიუთითეთ თქვენი სახელი: ")
        print(f'გამარჯობა {self.name}!')

    def choose_item(self):
        self.products = {'brown':9,"bouty":10,"cheescake":11}
        print('დღევანდელი პროდუქტების სია: ')        
        for i in self.products:
            print(i)
        self.product_name = str(input('მიუთითეთ სასურველი პროდუქტი: ')) # ისედაც სტრინგია ვიცი მაგრამ მაინც დამჭირდა ტერმინალი ცვლადად აღიქვამდა
        self.product_count = int(input('გთხოვთ მიუთითოთ რაოდენობა: ')) 
    
    def checkout(self):
        product_price = self.products[self.product_name]
        full_price = product_price  *self.product_count
        print(f"{self.name} თქვენ გადასახდელი გაქვთ {full_price} ლარი,")
        print('მადლობა რომ ხართ ჩვენი მომხმარებელი')



game = shop_game()
game.choose_item()
game.checkout()

