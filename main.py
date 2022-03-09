import random

def generateCode(type):
    code = ''
    characters = 'abcdefghijkmnprstuvwz123456789'
    charactersLength = len(characters)

    for i in range(6):
        code += characters[random.randrange(0, charactersLength)]

    if type == 1:
        code = code + '1b'
    elif type == 2:
        code = code + '2b'
    elif type == 3:
        code = code + '2s'
    elif type == 4:
        code = code + '3g'
    elif type == 5:
        code = code + '3s'
    elif type == 6:
        code = code + '3b'
    elif type == 7:
        code = code + '4g'
    elif type == 8:
        code = code + '5b'
    elif type == 9:
        code = code + '6s'
    elif type == 10:
        code = code + '9g'
    elif type == 11:
        code = code + '0s'
    else:
        code = code + '0g'

    return code


def getAmount(type):
    amounts = {
        1: 1000,
        2: 1500,
        3: 2000,
        4: 3000,
        5: 3000,
        6: 3000,
        7: 4500,
        8: 5000,
        9: 6000,
        10: 9000,
        11: 10000,
        12: 15000
    }
    return amounts[type]


def generateScript(numberOfCodes):
    query = 'INSERT INTO coupon_codes(code, amount, type_id, created_at, updated_at) values '
    values = ''

    def addValue(type, values):
        val = f'\n(\'{generateCode(type)}\', {getAmount(type)}, {type}, now(), now()),'
        return values + val

    for i in range(numberOfCodes):
        if i < 5000:
            type = 1
            values = addValue(type, values)
        elif i >= 5000 and i < 9000:
            type = 2
            values = addValue(type, values)
        elif i >= 9000 and i < 13000:
            type = 3
            values = addValue(type, values)
        elif i >= 13000 and i < 19000:
            if i < 15000:
                type = 4
                values = addValue(type, values)
            elif i >= 15000 and i < 17000:
                type = 5
                values = addValue(type, values)
            else:
                type = 6
                values = addValue(type, values)
        elif i >= 19000 and i < 22000:
            type = 7
            values = addValue(type, values)
        elif i >= 22000 and i < 24000:
            type = 8
            values = addValue(type, values)
        elif i >= 24000 and i < 26000:
            type = 9
            values = addValue(type, values)
        elif i >= 26000 and i < 28000:
            type = 10
            values = addValue(type, values)
        elif i >= 28000 and i < 29000:
            type = 11
            values = addValue(type, values)
        else:
            type = 12
            values = addValue(type, values)
    val = f'\n(\'{generateCode(12)}\', {getAmount(12)}, {12}, now(), now())'
    values += val

    return query + values


numberOfCodes = 30000
result = generateScript(numberOfCodes)

with open('inserts.txt', 'w') as f:
    f.write(result)
f.close()

