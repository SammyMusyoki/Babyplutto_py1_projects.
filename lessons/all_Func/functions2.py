# Collecting an arbitrary number of arguments

def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)


# Make three pizzas with different toppings.

make_pizza('small', 'pepperoni')
make_pizza('medium', 'bacon bits', 'pineapple')
make_pizza('large', 'mushrooms', 'peppers', 'onions', 'extra cheese')

