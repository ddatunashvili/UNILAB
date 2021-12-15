# დავალება 1
# დაწერეთ ფუნქცია რომელიც პარამეტრად მიიღებს Dict -ს და დაბეჭდავს პროდუქტის ინდექსს, პროდუქტს და ფასს, ასეთი ფორმატით: "{index}. {product} - {price}"
# მაგალითი:
"""
print_dict(products)
1. brown - 9.15
2. bounty - 11.5
3. cheesecake - 15.99
"""

# products
products = {
    "brown": 9.15,
    "bounty": 11.5,
    "cheesecake": 15.99
}

def print_dict(products):
    for i,object in enumerate(products):
        print(f"{i+1}. {object} - {products[object]}")


# დავალება 2
# დაწერეთ ლამბდა ფუნქცია რომელიც დააბრუნებს რიცხვისი კუბს
# მაგალითი: cube(2) -> 8
cube = "Write Lambda here"

cube = lambda x: x**3

# დავალება 3
# დაწერეთ ფუნქცია, რომელიც მიიღებს პარამეტრად ერთ რიცხვს და დააბრუნებს მნიშვნელობებს even/odd (String-ად) რიცხვის შესაბამისად
# მაგალითი: singleEvenOdd(3) -> 'odd', singleEvenOdd(2) -> 'even'
def singleEvenOdd(x):
    if (x % 2) == 0:
        return "even"
    else:
        return "odd"


# დავალება 4 (დამოკიდებულია დავალება 3 -ზე)
# დაწერეთ while ციკლი რომელიც მიიღებს მთელ რიცხვს და ყოველ იტერაციაზე დააკლებს მნიშვნელობას (და გაჩერდება თუ მიაღწევს ნულს) და List-ში შეინახავს typle წყვილებს, სადაც პირველი იქნება რიცხვი, მეორე კი სიტყვა even/odd 
# მაგალითი: evenOdd(5) -> [(5, 'odd'), (4, 'even'), (3, 'odd'), (2, 'even'), (1, 'odd')]
def evenOdd(n):
    listt =[]
    while 0 < n:
        if (n % 2) != 0:
            tupl =(n,"odd") 
            listt.append(tupl)
        else:
            tupl =(n,"even") 
            listt.append(tupl)
        n -= 1
    return listt
# დავალება 5
# დაწერეთ list comprehension-ის მეშვეობით ფუნქცია, რომელიც მასივის ყოველ ელემენტს აახარიხებს მეორე ხარისხში და დაგვიბრუნებს ახარისხებულ ლისტს. 
# მაგალითი: powerList([1, 2, 3]) -> [1, 4, 9] 
def powerList(lst):
    new = []
    for num in lst:
        new.append(num**2)
    return new


# დავალება 6
# დაწერეთ list comprehension-ის მეშვეობით ფუნქცია, რომელიც ორი ლისტის ელემენტებს გააერთიანებს წინადადებებად და დაგვიბრუნებს გაერთიანებულ სთრინგებს ლისტში. 
# მაგალითი: string_mix(["John,", "Jane,"], ["Hello!", "How are you?"]) -> ['John, Hello!', 'John, How are you?', 'Jane, Hello!', 'Jane, How are you?']
 
def string_mix(lst1, lst2):
    new = []
    for name in lst1:
        for hello in lst2:
           new.append([f"{name} {hello}"])
    return new
if __name__ == "__main__":
    print_dict(products)
    print(cube(2))
    print(singleEvenOdd(5))
    print(evenOdd(5))
    print(powerList([1, 2, 3]))
    print(string_mix(["Jhon,", "Jane,"], ["Hello!", "How are you?"]))