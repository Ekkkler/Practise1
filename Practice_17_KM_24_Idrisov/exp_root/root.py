

def root2(a):
    return a ** 0.5

def root3(a):    
    def sign(num):
        return 1 if num >= 0 else -1

    return sign(a) * (abs(a) ** (1/3))
