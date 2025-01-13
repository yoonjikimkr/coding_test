import re
def num_chk (func) :
    def inside(*args,**kwargs):
        nos=func(*args)
        for i in nos:
            if not re.match(r'^[A-Z][0-9]{10}(M|B|H)$', i):
                print("Invalid")
            else:
                print("Valid")
    return inside

@num_chk
def fetch_phn_nos(phn_nos):
    return phn_nos
fetch_phn_nos (['A1234567890M', 'M98765432101H', 'H1234562950Z', 'X384783375B'])