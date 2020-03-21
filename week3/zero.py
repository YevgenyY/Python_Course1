import traceback

try:
    #raise "Value error"
    print(1/0)
except:
    print("Zero division error")
    traceback.print_exc("")
