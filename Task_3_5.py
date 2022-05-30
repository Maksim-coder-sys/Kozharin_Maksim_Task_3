import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
my_list = []


def get_jokes(number = 1, flag = 0):
    """a function that returns n jokes formed from three random words"""
    my_nouns = nouns[:]
    my_adverbs = adverbs[:]
    my_adjectives = adjectives[:]
    for i in range(number):
        if flag == 1:
            my_nouns_index = random.randint(0, len(my_nouns) - 1)
            my_nouns_word = my_nouns[my_nouns_index]
            my_nouns.pop(my_nouns_index)
            my_adverbs_index = random.randint(0, len(my_adverbs) - 1)
            my_adverbs_word = my_adverbs[my_adverbs_index]
            my_adverbs.pop(my_adverbs_index)
            my_adjectives_index = random.randint(0, len(my_adjectives) - 1)
            my_adjectives_word = my_adjectives[my_adjectives_index]
            my_adjectives.pop(my_adjectives_index)
            element = my_nouns_word + ' ' + my_adverbs_word + ' ' + my_adjectives_word
            my_list.append(element)
        else:
            nouns_index = random.randint(0, len(nouns) - 1)
            nouns_word = nouns[nouns_index]
            adverbs_index = random.randint(0, len(adverbs) - 1)
            adverbs_word = adverbs[adverbs_index]
            adjectives_index = random.randint(0, len(adjectives) - 1)
            adjectives_word = adjectives[adjectives_index]
            element = nouns_word + ' ' + adverbs_word + ' ' + adjectives_word
            my_list.append(element)

    return my_list

print(get_jokes(5,1))
