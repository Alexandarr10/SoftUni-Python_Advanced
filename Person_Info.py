def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

person = {'age' : 20, 'name': "Peter"}
some_func = (person['name'], person['age'])
some_func(**person)

