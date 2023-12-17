#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) != str:
            print("The value must be a string.")
        else:
            self._value = value  

    def is_sentence(self):
        return self.value.endswith('.')
        pass

    def is_question(self):
        return self.value.endswith('?')
        pass

    def is_exclamation(self):
        return self.value.endswith('!')
        pass

    def count_sentences(self):
        word_list = self.value.split(" ")
        print(word_list)
        count = 0

        for word in word_list:
            print(word)
            word = MyString(word)
            if word.is_sentence():
                count += 1
                del word

            elif word.is_question():
                count += 1
                del word

            elif word.is_exclamation():
                count += 1
                del word

            else:
                del word

        return count