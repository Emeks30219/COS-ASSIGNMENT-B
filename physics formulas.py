
print("choose a formula:")
print("a= momentum (M=m*v)")
print("b= potential energy (PE=m*g*h)")
print("c= ohms law (V= I*R)")
print("d= kinetic energy (KE=0.5*m*v^2)")
print("e=work done(w=f*d")

choice = input("Enter a,b,c,d or e: " )
choice = choice.lower()
if choice == "a":
    m= float(input("mass m:"))
    v= float(input("velocity v:"))
    M= m*v
    print("momentum", M)
elif choice == "b":
    m=float(input("mass m:"))
    g= float(input("gravity g:"))
    h= float(input("height h:"))
    PE=m*g*h
    print("potential energy", PE)
elif choice == "c":
    I= float(input("current I :"))
    R= float(input("resistance R :"))
    V= I*R
    print("Voltage", V)
elif choice == "d":
    m= float(input("mass, m:"))
    v= float(input("velocity, v:"))
    KE = 0.5*m*v**2
    print("kinetic energy", KE)
elif choice == "e":
    f=float(input("force, f:"))
    d=float(input("distance, d:"))
    w=f*d
    print("work done", w)
else:(print("INVALID CHOICE"))















