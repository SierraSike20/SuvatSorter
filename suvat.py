def one(v, u, a, t):
    print(str(v + " = " + u + " + " + a + " * " + t))

def two(s, u, v, t):
    print(str(s + " = " + " ( " + u + " + " + v + " ) " + " * " + " 1/2 " + " * " + t))

def three(v, u, a, s):
    print(str(v + "^2 " + " = " + u + "^2 " + " + " + " 2 " + "*" + a + " * " + s))

def four(s, u, t, a):
    print(str(s + " = " + u + " * " + t + " + " + a + " * " + t + "^2 " + "*" + " 1/2 "))

def five(s, v, t, a):
    print(str(s + " = " + v + " * " + t + " - " + a + " * " + t + "^2 " + " * " + " 1/2 "))


print("SUVAT Calculator, assuming constant acceleration\n"
      "a - acceleration\n"
      "v - final velocity\n"
      "u - initial velocity\n"
      "s - displacement\n"
      "t - time\n")

# 1  v = u + at
# 2  s = 1/2(u + v)t
# 3  v^2 = u^2 + 2as
# 4  s = ut + at^2 / 2
# 5  s = vt - at^2 / 2

goal = str(input("What are you trying to find?\n"))

while goal.strip().lower() != "s" \
        and goal.strip().lower() != "a" \
        and goal.strip().lower() != "t" \
        and goal.strip().lower() != "v" \
        and goal.strip().lower() != "u":
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

        t = float(t)
        v = float(v)
        u = float(u)
    
        s = ((u + v) * 0.5) * t
        print("\n The displacement is: " + str(s) + "m")

    elif t == "none":
    #take 3
        three(v, u, a, s)

        a = float(a)
        v = float(v)
        u = float(u)
    
        s = (((v**2) - u**2) / 2) / a
        print("\n The displacement is: " + str(s) + "m")
    
    elif v == "none":
    #take 4
        four(s, u, t, a)

        a = float(a)
        t = float(t)
        u = float(u)
        
        s = (u * t) + ((a * (t**2)) / 2)
        print("\n The displacement is: " + str(s) + "m")

    elif u == "none":
    #take 5
        five(s, v, t, a)

        a = float(a)
        t = float(t)
        v = float(v)
        
        s = (v * t) - ((a * (t**2)) / 2)
        print("\n The displacement is: " + str(s) + "m")
    
    else:
        print("=======================================\n"
              "You entered too few or too many values.\n"
              "=======================================")

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

        t = float(t)
        v = float(v)
        u = float(u)
    
        a = (v - u) / t
        print("\nThe acceleration is: " + str(a) + "m/s^2")
    
    elif t == "none":
    #take 3
        three(v, u, a, s)

        s = float(s)
        v = float(v)
        u = float(u)
    
        a = ((v**2 - u**2) / 2) / a
        print("\nThe acceleration is: " + str(a) + "m/s^2")
    
    elif v == "none":
    #take 4
        four(s, u, t, a)

        s = float(s)
        t = float(t)
        u = float(u)
        
        a = ((s - (u * t)) * 2) / t**2
        print("\nThe acceleration is: " + str(a) + "m/s^2")
        
    elif u == "none":
    #take 5
        five(s, v, t, a)

        s = float(s)
        t = float(t)
        v = float(v)
        
        a = ((s - (v * t)) * -2) / t**2
        print("\nThe acceleration is: " + str(a) + "m/s^2")
    
    else:
        print("=======================================\n"
              "You entered too few or too many values.\n"
              "=======================================")

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

        a = float(a)
        v = float(v)
        u = float(u)
    
        t = (v - u) / a
        print("\nThe time is: " + str(t) + "s")

    elif a == "none":
    #take 2
        two(s, u, v, t)

        s = float(s)
        v = float(v)
        u = float(u)
    
        t = ((s * 2) / (u + v))
        print("\nThe time is: " + str(t) + "s")
    
    elif v == "none":
    #take 4
        four(s, u, t, a)

        s = float(s)
        a = float(a)
        u = float(u)
        
        if u == 0:
            t = (s / (0.5 * a))**0.5
            print("\nThe time is: " + str(t) + "s")
        else:
            print("\nYour equation is quadratic.")
        
    elif u == "none":
    #take 5
        five(s, v, t, a)

        s = float(s)
        a = float(a)
        v = float(v)
    
        if v == 0:
            t = (s / (-0.5 * a))**0.5
            print("\nThe time is: " + str(t) + "s")
        else:
            print("\nYour equation is a quadratic.")
    
    else:
        print("=======================================\n"
              "You entered too few or too many values.\n"
              "=======================================")

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

        a = float(a)
        t = float(t)
        u = float(u)
    
        v = u + (a * t)
        print("\nThe final velocity is: " + str(v) + "m/s")

    elif a == "none":
    #take 2
        two(s, u, v, t)

        s = float(s)
        t = float(t)
        u = float(u)
    
        v = ((s / t) * 2) - u
        print("\nThe final velocity is: " + str(v) + "m/s")
        
    elif t == "none":
    #take 3
        three(v, u, a, s)

        s = float(s)
        a = float(a)
        u = float(u)
    
        v = ((u**2) + (2 * a * s))**0.5
        print("\nThe final velocity is: " + str(v) + "m/s")
    
    elif u == "none":
    #take 5
        five(s, v, t, a)

        s = float(s)
        a = float(a)
        t = float(t)
    
        v = (s + (0.5 * a * t**2)) / t
        print("\nThe final velocity is: " + str(v) + "m/s")
    
    else:
        print("=======================================\n"
              "You entered too few or too many values.\n"
              "=======================================")

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

        a = float(a)
        t = float(t)
        v = float(v)

        u = v - (a * t)
        print("\nThe initial velocity is: " + str(u) + "m/s")

    elif a == "none":
    #take 2
        two(s, u, v, t)

        s = float(s)
        t = float(t)
        v = float(v)

        u = ((s / t) * 2) - v
        print("\nThe initial velocity is: " + str(u) + "m/s")

    elif t == "none":
    #take 3
        three(v, u, a, s)

        s = float(s)
        a = float(a)
        v = float(v)

        u = ((v**2) - (2 * a * s))**0.5
        print("\nThe initial velocity is: " + str(u) + "m/s")

    elif v == "none":
    #take 4
        four(s, u, t, a)

        s = float(s)
        a = float(a)
        t = float(t)

        u = (s - (0.5 * a * t**2)) / t
        print("\nThe initial velocity is: " + str(u) + "m/s")
    
    else:
        print("=======================================\n"
              "You entered too few or too many values.\n"
              "=======================================")