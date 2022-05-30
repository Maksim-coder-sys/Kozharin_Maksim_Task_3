def thesaurus(*args):
    """creating a dictionary of arguments where the key is the first
     letter of the argument, and the value is the argument itself"""
    rez = {}
    for arg in args:
        arg = arg.capitalize()
        key = arg[0]
        if not key in rez:
            rez[key] = []
            rez[key].append(arg)
        else:
            rez[key].append(arg)
    print(dict(sorted(rez.items())))
    return rez
print(thesaurus('Иван','Максим','Михаил','Людмила','Инна','лена','Женя'))





