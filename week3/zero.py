try:
    raise "ValueError"
    print(1/0)
except:
    print("Zero division error")
