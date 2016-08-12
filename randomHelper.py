import random
import string

class RandomHelper():

    def random_int_generator(self, size = 10, chars = string.digits):
        return ''.join(random.choice(chars) for x in range(size))


    def random_string_generator(self, size = 10, chars = string.letters):
        return ''.join(random.choice(chars.capitalize()) for x in range(size))
