while True:
    try:
        raw = input("enter a bumber: ")
        number = int(raw)
        break
    except ValueError:
        print("You have entered something strange!")
    except (KeyboardInterrupt, ZeroDivisionError):
        print("Exit")
        break
    finally:
        print("Finally")

print( issubclass(KeyError, LookupError) )
print( issubclass(IndexError, LookupError) )

