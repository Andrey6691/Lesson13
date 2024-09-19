calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = list(map(str.upper,list_to_search))
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Lemonad'))
print(string_info('Robot'))
print(is_contains('Agregat', ['agREgat', 'Fregat', 'Generator']))
print(is_contains('Radiator', ['raDiAtor', 'Gladiator', 'Radio']))
print(is_contains('Globus', ['Opus', 'avtobus']))
print(calls)
