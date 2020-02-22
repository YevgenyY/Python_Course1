import sys

if (not len(sys.argv) > 1):
    sys.exit("gimme some data")

digit_string = sys.argv[1]

accum = 0

for n in digit_string:
    num = int(n)
    accum += num

print(accum)

