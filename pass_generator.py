import random
from random import randrange
import array

class PassGenerator:
    arr_random_symbol = ['q', 'w', 'e', 'r', 't', 'y',
                         'u', 'i', 'o', 'p', 'a', 's',
                         'd', 'f', 'g', 'h', 'j', 'k',
                         'l', 'z', 'x', 'c', 'v', 'b',
                         'n', 'm',
                         '[', ']', ')', '(', '&', '^',
                         '!', '@', '#', '%', '~', '=',
                         '?', '>', '<', '{', '}', '/',
                         '`', '"', ';', ':', ',', '.']


    def __init__(self):
        pass

    def random_generator(self, length_pass: str) -> str:
        if not length_pass.isnumeric():# любой символ кроме цифры -> return 'Invalid'
            return 'Invalid'

        number = int(length_pass)

        if number < 1:
            return 'Invalid'

        password = ''

        for i in range(number):
            random = randrange(len(self.arr_random_symbol))
            password += self.arr_random_symbol[random]

        return password
        #return ''.join(random.sample(self.arr_random_symbol, int(length_pass)))

