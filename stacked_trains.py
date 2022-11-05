# v between trains is held as constant

C = 3*10**8 #speed of light

def sequence(v):
    u = 0

    while True: 
        yield u
        u = (v + u)/(1 + v*u/(C*C))


def print_terms(x,y):
    for n, u in enumerate(sequence(v=y)):
        print(f"u({n}) = {u}")
        if n >= x:
            break

if __name__ == "__main__":
    print_terms(50,10)