
print("Four Credit Subjects are  40 CS 601")
print("Four Credit Subjects are  40 CS 602")

k = []
p = []
u = []
y = []

a = int(input("Enter number of four credit subjects:"))
b = int(input("Enter number of three credit subjects:"))
c = int(input("Enter number of two credit subjects:"))
for i in range(a):
    fcsub = input("enter grade (4credit):")
    k.append(fcsub)
    k[i] = fcsub.upper()

    if k[i] == 'S' :
        k[i] = 10 * 4

    elif k[i] == 'A' :
        k[i] = 9 * 4

    elif k[i] == 'B' :
        k[i] = 8 * 4

    elif k[i] == 'C' :
        k[i] = 7 * 4

    elif k[i] == 'D' :
        k[i] = 6 * 4

    elif k[i] == 'E' :
        k[i] = 5 * 4

    elif k[i] == 'RA' :
        k[i] = 0 * 4

    else:
        print("error")
for i in range(b):
    tcsub = input("enter grade (3credit):")
    p.append(tcsub)
    p[i] = tcsub.upper()

    if p[i] == 'S' :
        p[i] = 10 * 3

    elif p[i] == 'A' :
        p[i] = 9 * 3

    elif p[i] == 'B' :
        p[i] = 8 * 3

    elif p[i] == 'C' :
        p[i] = 7 * 3

    elif p[i] == 'D' :
        p[i] = 6 * 3

    elif p[i] == 'E' :
        p[i] = 5 * 3

    elif p[i] == 'RA' :
        p[i] = 0 * 3

    else:
        print("error")
for i in range(c):
    twcsub = input("enter grade (2credit):")
    u.append(twcsub)
    u[i] = twcsub.upper()

    if u[i] == 'S' :
        u[i] = 10 * 2

    elif u[i] == 'A' :
        u[i] = 9 * 2

    elif u[i] == 'B' :
        u[i] = 8 * 2

    elif u[i] == 'C' :
        u[i] = 7 * 2

    elif u[i] == 'D' :
        u[i] = 6 * 2

    elif u[i] == 'E' :
        u[i] = 5 * 2

    elif u[i] == 'RA' :
        u[i] = 0 * 2

    else:
        print("error")
xtsub = input("enter grade (0credit):")
for i in k:
##    e = i/((len(k) * 4) + (len(p) * 3) + (len(u) * 2))
    y.append(i)
for i in p:
##    e = i/((len(k) * 4) + (len(p) * 3) + (len(u) * 2))
    y.append(i)
for i in u:
##    e = i/((len(k) * 4) + (len(p) * 3) + (len(u) * 2))
    y.append(i)
print (sum(y))
print ((len(k) * 4) + (len(p) * 3) + (len(u) * 2))
SGPA = (sum(y)) / ((len(k) * 4) + (len(p) * 3) + (len(u) * 2))
print("SGPA:",SGPA)
ocgpa = float(input("Enter old CGPA:"))
numsematt = int(input("Enter number of sem attended:"))

CGPA = (ocgpa * numsematt + SGPA) / (numsematt + 1)
print("CGPA:",CGPA)
