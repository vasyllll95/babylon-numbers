
def package_number_to_babylon(number):
    parsed_number = _parse_number(number)
    return " ".join(map(lambda number: _number_to_babylon(number[0]), parsed_number[::-1])) 

def _number_to_babylon(number):
    if number > 59:
        raise Exception("Babylon number part can be less than 59.")
    decimals = int(number/10)
    return "<" *decimals +"Y" * int(number - decimals * 10)

def _parse_number(number):
    if number < 0:
        raise Exception("Cannot operate with negative number.")
    res=[]
    index = 0
    while number >= 60:
        res.append((int(number % 60), index))
        number/=60
        index+=1
    res.append((int(number),index))
    return res
