import sys

def make_str(num, len):
    line = ""
    for i in range(num):
        line += "#"
    
    format_str = '{:>' + str(len) + '}'
    #return '{:>5}'.format(str)
    return format_str.format(line)


if (not len(sys.argv) > 1):
    sys.exit("gimme some data")

len = int(sys.argv[1])

for n in range( 1, len+1 ):
    line = make_str( n, len )
    print(line)


