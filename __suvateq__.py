def one(v, u, a, t):
    return str(v + "=" + u + "+" +  a + "*" + t)

def two(s, u, v, t):
    return str(s + "=" + "(" + u + "+" + v + ")" + "*" + "1/2" + "*" + t)

def three(v, u, a, s):
    return str(v + "^2" + "=" + u+ "^2" + "+" + "2" + "*" + a + "*" + s)

def four(s, u, t, a):
    return str(s + "=" + u + "*" + t + "+" + a + "*" + t + "^2" + "*" + "1/2")

def five(s, v, t, a):
    return str(s + "=" + v + "*" + t + "-" + a + "*" + t + "^2" + "*" + "1/2")
