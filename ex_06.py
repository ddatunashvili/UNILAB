students = [{
            "name":"john",
            "age":"19",
            "gender":"m", # მონაცემის დანაკლისი შეცდომა არ არის 
            "course":"2",
            },{
            "name":"Carla",
            "age":"21",
            "gender":"f",
            "university": None,
            "course":"2",
            },{
            "name":"Jane",
            "age":"18",
            "gender":"f",
            "university":"ilia state university",
            "course":"2",
            },{
            "name":"Carlos",
            "age":"17",
            "gender":"m",
            "university":"ilia state university",
            "course":"2",
            }
            ]


def getPerson(lst, name):
    """ ფუნქცია იღებს 2 პარამეტრს, სტუდენტების სიას და სახელს, და ბეჭდავს სახელსი შესაბამის ინფორმაციას. 
        უნივერსიტეტის არ არსებობის შემთხვევაში, დაბეჭდოს ilia state university
    """
    for object in lst:
        if object['name'] == name:
            if 'university' not in object  or object['university'] == None:
                print("ilia state university")
            else:
                print(object)


def intro(*args, **kwargs):
    """ ფუნქცია უნდა ბეჭდავდეს სახელს და გვარს პირველი პარამეტრიდან, მეორე კი დამატებით ინფორმაციას ადამიანზე.
        უნდა აბრუნებდეს წინადადებას: 
        გამარჯობა მე მქვია {სახელი} {გვარი}. 
        ცოტა რამ ჩემს შესახებ:
        {key}:{value},
        {key}:{value},
        {key}:{value},
        {key}:{value},
    """
    name, surname =  args
        

    print(f'გამარჯობა მე მქვია {name} {surname}.')
    print('ცოტა რამ ჩემს შესახებ:')
    for key, value in kwargs.items():
        print(f'{key}:{value},')

def myGenerator(n):
    """ ფუნქცია აბრუნებს გენერატორს, რომელიც იქმნება while ციკლის მეშვეობით, პარამეტრში მითითებულ რიცხვამდე """
    while 0 < n:
        n-=1
        yield  n



# Generator expression
# შექმენით გენერატორი რომელიც დააგენერირებს რიცხვებს მითითებულ რიცხვამდე და დაგვიბრუნებს დაგენერირებული რიცხვების ჯამს.
def generatedSum(n):
    sum = 0
    while 0 < n: 
        n-=1
        sum += n
    yield sum

if __name__ == "__main__":
    getPerson(students, "john")
    getPerson(students, "Jane")
    getPerson(students, "Carla")
    intro("David", "Chincharashvili", hobby='Painting', profession="Programmer")
    print(list(myGenerator(20)))
    print(list(generatedSum(6))) # აქ ლისტში გადავიყვანე რომ გენერატორის ობიექტის  აუთფუთი რიცხვი ყოფილიყო 15 და არა ობიექტი თორე ფუნქციის აუთფუთის ტიპი გენერატორია