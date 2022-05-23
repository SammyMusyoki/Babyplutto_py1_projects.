from lessons.Pizza_Inn import pizza
users = []

new_user = {
    'last_name': input('Enter last name: '),
    'first_name': input('Enter first name: '),
    'username': input('Enter username: '),
}
users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print('\n')


pizza.make_pizza('small', 'pepperoni')
pizza.make_pizza('medium', 'bacon bits', 'Onions', 'extra cheese')