from pprint import pprint
answer = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]

pprint(answer)
