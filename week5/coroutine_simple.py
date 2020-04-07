def grep(pattern):
    print("start grep")

    try:
        while True:
            line = yield
            if pattern in line:
                print(line)

    except GeneratorExit:
        print('stop grep')

g = grep("python")

next(g) # g.send(None)
g.send('golang is better')
g.send('python is simple')
g.close()

def grep_pep0380():
    g = grep("python")
    yield from g

g = grep_pep0380() # is g a coroutine?
print(g)

g.send(None)
g.send('python is the good!')


