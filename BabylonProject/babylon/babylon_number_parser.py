

def parse_babylon(babylon_number: str):
    '''
        Parameters: 
    '''
    result_number = 0
    for index, number_part in enumerate(babylon_number.split()[::-1]):
        if index < 1:
            result_number+=get_number_part(number_part)
            continue
        result_number+=(get_number_part(number_part)*60**index)
    return result_number

def get_number_part(string_part):
    return sum(map(convert_babylon_symbol_to_number,list(string_part)))

def convert_babylon_symbol_to_number(symbol):
    if symbol == '<':
        return 10
    elif symbol == 'Y':
        return 1
    return 0

