import sys

numbers = sys.argv
try:
    numbers = list(map(lambda x: float(x), numbers[1:]))
except:
    print("wrong input , only integers and floats")

print(sum(numbers) / len(numbers))
