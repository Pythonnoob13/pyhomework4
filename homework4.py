keys: list = ['Ten', 'Twenty', 'thirty']
values: list = [10, 20, 30]
dic: dict = dict(zip(keys, values))

print(dic)

dict1: dict = {'Ten': 10, 'Twenty': 20, 'thirty': 30}
dict2: dict = {'thirty': 30, 'fourty': 40, 'fifty': 50}
dict1.update(dict2)
print(dict1)

dictionary = {'username':[], 'age':[], 'adress':[]}
username = input('please enter username: ').title()
age = input('please enter age: ')
adress = input('please enter adress: ').title()
dictionary['username'].append(username)
dictionary['age'].append(age)
dictionary['adress'].append(adress)
print(dictionary)


employee = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New york'
}
employee.pop('name', 'salary')
print(employee)






available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = []
final_toppings = []

def get_toppings():
    while True:
        input_toppings = input(f'please choose toppings {available_toppings} and press Done: ').lower()

        if input_toppings == 'done':
            return requested_toppings
        requested_toppings.append(input_toppings)
get_toppings()

def checker():
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
            final_toppings.append(requested_topping)
        elif requested_topping not in available_toppings:
            answer = input(f'we dont have {requested_topping} would u like a pizza without it? Yes/No - ').upper()
            if answer == answer == 'NO':
                print('we are sorry, see u next time!')
                break
            elif answer == 'YES':
                continue

checker()
def final():

    if len(final_toppings) > 0:
        print(f'your pizza with {final_toppings} is done')
    else:
        print("Your pizza without topping is done")
        quit()
final()