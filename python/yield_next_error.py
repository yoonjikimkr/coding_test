nos=(i for i in range (10))
def generate_nos (mynos) :
    for i in mynos:
        yield i*2 # yield vs. return: yield returns a generator object, return returns a value
try:
    while (1):
        if next(generate_nos(nos))==18: # next() function returns the next item from the iterator
            print (next(generate_nos (nos)))
except AssertionError:
    print("AssertionError occured")
except StopIteration:
    print("StopIteration raised")
except TypeError:
    print ("TypeError occured")