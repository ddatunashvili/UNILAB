import sys
"""
1) შექმენით ფუნქცია რომელიც სამ ინდივიდუალურ რიცხვით არგუმენტს შორის უდიდესს დააბრუნებს.
- არ გამოიყენოთ პითონის ჩაშენებული ფუნქციები ან მონაცემთა სტრუქტურები (ლისტი, თაფლი...)
"""

def custom_max(a,b,c):
    if c == a or  c == b or a == b:
        return "Incorrect parameters: There are some equal values in parameters"       
    elif b > a  and b > c:
        return b
    elif c > a  and c > b:
        return c
    elif a > b and a > c: 
        return a
    else:
        return 'eror 404 not found'
    
print(custom_max(1,2,4))

"""
2) შექმენით ფუნქცია რომელსაც გადასცემთ ტექსტს (ლათინური ასოებით), ხოლო უკან დააბრუნებს Tuple-ს ([ხმოვნები], [თანხმოვნები]): 
მაგალითი: vowel_consonant("abc") -> (["a"],["b","c"])
https://www.w3schools.com/python/python_ref_string.asp
"""
def vowel_consonant(str):
    vowels = ['a','e','i','o','u']
    consonants = []
    non_consonants = []
    for char in str:
        if char in vowels:
            non_consonants.append(char)
        else:
            consonants.append(char)
    return (non_consonants,consonants)
print(type(vowel_consonant('abc')))

"""
3) დაწერეთ ფუნქცია რომელიც List-იდან ამოიღებს კონკრეტულ ელემენტს და დააბრუნებს ახალ List-ს მითითებული ელემენტის გარეშე
მაგალითი: custom_filter([1,2,3,4,4,4,4,4,5], 4) -> [1,2,3,5]
"""
def custom_filter(lst, item):
    ordered = []
    for num in lst:
        if num != item:
            ordered.append(num)
    return ordered

print(custom_filter([1,2,3,4,4,4,4,4,5], 4))


"""
4) დაწერეთ ფუნქცია რომელიც შეაჯამებს ყველა რიცხვს List-ში (for ციკლის მეშვეობით)
მაგალითი: custom_sum([1,2,3,4,5]) -> 15
"""
def custom_sum(lst):
    sum = 0
    for num in lst:
        sum+=num
    return sum

print(custom_sum([1,2,3,4,5]))

"""
5) დაწერეთ ფუნქცია რომელიც დააბრუნებს List-ის უნიკალურ ელემენტებს List-ად (type casting -ის მეშვეობით)
მაგალითი: custom_unique_lst([1,2,2,3,4,5,3,4,5]) -> [1,2,3,4,5]
"""

def custom_unique_lst(lst):
    lst = list(set(lst))
    return lst

print(custom_unique_lst([1,2,2,3,4,5,3,4,5]))

"""
6) დაწერეთ ფუნქცია რომელიც ჩადგმული ციკლის (Nested Loop) მეშვეობით დაგვიბრუნებს გამრავლების ტაბულას მითითებულ რიცხვამდე
მაგალითი: custom_mult_table(10) ფუნქციის შედეგი იქნება მიმაგრებულ ფაილში
https://www.w3schools.com/python/gloss_python_escape_characters.asp
"""
def custom_mult_table (n):
    for a in range(1, n+1):
        for b in range(1,n+1):
            print(f"| {a*b:2d} ", end='',)
        print()  
    

if __name__ == "__main__":
    custom_mult_table(int(sys.argv[1])) # კარგად ვერ მივხვდი რა იგულისხმე შედეგი ფაილშიო და ესე გავაკეთე