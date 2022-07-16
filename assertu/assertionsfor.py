import random
import string
import names

rand_name = names.get_first_name(gender='male')
rand_lastname = names.get_last_name()
password_random = ''.join(random.choice(string.ascii_letters) for i in range (8))
class Assertion:

    name = (rand_name)
    last_name = (rand_lastname)
    email = (rand_lastname + '_'+ rand_name + '@gmail.com')
    password = (password_random)