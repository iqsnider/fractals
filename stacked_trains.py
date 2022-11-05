# v between trains is held as constant

C = 3*10**8 #speed of light

def sequence(v):
    u = 0

    while True: 
        yield u
        u = (v + u)/(1 + v*u/(C*C))

for n, u in enumerate(sequence(v=100)):
    print(f"u({n}) = {u}")
    if n >= 50:
        break