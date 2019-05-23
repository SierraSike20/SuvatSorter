def one(v, u, a, t):
    print(str(v + " = " + u + " + " +  a + " * " + t))

def two(s, u, v, t):
    print(str(s + " = " + " ( " + u + " + " + v + " ) " + " * " + " 1/2 " + " * " + t))

def three(v, u, a, s):
    print(str(v + "^2 " + " = " + u+ "^2 " + " + " + " 2 " + "*" + a + " * " + s))

def four(s, u, t, a):
    print(str(s + " = " + u + " * " + t + " + " + a + " * " + t + "^2 " + "*" + " 1/2 "))

def five(s, v, t, a):
    print(str(s + " = " + v + " * " + t + " - " + a + " * " + t + "^2 " + " * " + " 1/2 "))


print("SUVAT Calculator, assuming constant acceleration\na - acceleration\nv - final velocity\nu - initial velocity\ns - displacement\nt - time\n")

# 1  v = u + at
# 2  s = 1/2(u + v)t
# 3  v^2 = u^2 + 2as
# 4  s = ut + at^2 / 2
# 5  s = vt - at^2 / 2

goal = str(input("What are you trying to find?\n"))

while goal.strip().lower() != "s" and goal.strip().lower() != "a" and goal.strip().lower() != "t" and goal.strip().lower() != "v" and goal.strip().lower() != "u":
    goal = str(input("Enter a valid input\nWhat are you trying to find?\n"))


#-----------------------------------------------------------------------------------------------------------------------


print("if you do not know the value, put none")

if goal.strip().lower() == "s":
    a = str(input("What is the value of your acceleration?\n"))
    t = str(input("What is the time period?\n"))
    v = str(input("What is the final velocity?\n"))
    u = str(input("What is the initial velocity?\n"))
    s = "s"
    if a == "none":
    #take 2
        two(s, u, v, t)


    elif t == "none":
    #take 3
        three(v, u, a, s)


    elif v == "none":
    #take 4
        four(s, u, t, a)


    elif u == "none":
    #take 5
        five(s, v, t, a)


#-----------------------------------------------------------------------------------------------------------------------

if goal.strip().lower() == "a":
    s = str(input("What is the value of the displacement?\n"))
    t = str(input("What is the time period?\n"))
    v = str(input("What is the final velocity?\n"))
    u = str(input("What is the initial velocity?\n"))
    a = "a"

    if s == "none":
    #take 1
        one(v, u, a, t)

    elif t == "none":
    #take 3
        three(v, u, a, s)

    elif v == "none":
    #take 4
        four(s, u, t, a)

    elif u == "none":
    #take 5
        five(s, v, t, a)


#-----------------------------------------------------------------------------------------------------------------------

if goal.strip().lower() == "t":
    s = str(input("What is the value of the displacement?\n"))
    a = str(input("What is the value of your acceleration?\n"))
    v = str(input("What is the final velocity?\n"))
    u = str(input("What is the initial velocity?\n"))
    t = "t"

    if s == "none":
    #take 1
        one(v, u, a, t)

    elif a == "none":
    #take 2
        two(s, u, v, t)

    elif v == "none":
    #take 4
        four(s, u, t, a)

    elif u == "none":
    #take 5
        five(s, v, t, a)

#-----------------------------------------------------------------------------------------------------------------------

if goal.strip().lower() == "v":
    s = str(input("What is the value of the displacement?\n"))
    a = str(input("What is the value of your acceleration?\n"))
    t = str(input("What is the time period?\n"))
    u = str(input("What is the initial velocity?\n"))
    v = "v"

    if s == "none":
    #take 1
        one(v, u, a, t)

    elif a == "none":
    #take 2
        two(s, u, v, t)

    elif t == "none":
    #take 3
        three(v, u, a, s)

    elif u == "none":
    #take 5
        five(s, v, t, a)

#-----------------------------------------------------------------------------------------------------------------------

if goal.strip().lower() == "u":
    s = str(input("What is the value of the displacement?\n"))
    a = str(input("What is the value of your acceleration?\n"))
    t = str(input("What is the time period?\n"))
    v = str(input("What is the final velocity?\n"))
    u = "u"

    if s == "none":
    #take 1
        one(v, u, a, t)

    elif a == "none":
    #take 2
        two(s, u, v, t)

    elif t == "none":
    #take 3
        three(v, u, a, s)

    elif v == "none":
    #take 4
        four(s, u, t, a)
else:
    print("=======================================\nYou entered too few or too many values.\n=======================================")