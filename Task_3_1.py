number_dict = {'zero': 'ноль', 'one': 'один',
               'two': 'два', 'free': 'три',
               'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь',
               'eight': 'восемь', 'nine': 'девять',
                'ten':'десять'}

def num_translate(number_eng):
    """the number in English correlates itself with the Russian translation"""
    for key in number_dict.keys():
        if key == number_eng:
            return number_dict.get(number_eng)



print(num_translate('eleven'))

