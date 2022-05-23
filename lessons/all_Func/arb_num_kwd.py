# Collecting an arbitrary number of keyword arguments

def build_profile(first, last, **user_info):

    # Build a dictionary with the required keys

    profile = {'first': first, 'last': last}

    # Add any other keys and values.

    for key, value in user_info.items():
        profile[key] = value

    return profile

# Create two users with different kinds
# of information.


user_0 = build_profile('john', 'doe', location='princeton')
user_1 = build_profile('Erica', 'Stones',
                       location='paris', field='chemistry')
print(user_0)
print(user_1)




