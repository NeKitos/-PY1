# TODO решить с помощью list comprehension и распечатать его
answer = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]
from pprint import pprint

pprint(answer)