import math
from matplotlib import pyplot as plt
import numpy.random as rand


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def magnitude(self):
        mag = math.sqrt(self.x ** 2 + self.y ** 2)
        return mag

    def add(self, vector):
        xf = self.x + vector.x
        yf = self.y + vector.y
        return Vector(xf, yf)

    def subtract(self, vector):
        xf = self.x - vector.x
        yf = self.y - vector.y
        return Vector(xf, yf)

    def v_multiply(self, vector):
        xf = self.x * vector.x
        yf = self.y * vector.y
        return Vector(xf, yf)

    def s_multiply(self, c):
        xf = self.x * c
        yf = self.y * c
        return Vector(xf, yf)


class Planet:
    def __init__(self, mass, radius, pos, vel, name):
        self.name = name
        self.r = radius
        self.m = mass
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.vel = vel
        self.momentum =  vel.s_multiply(self.m)

    def force(self, planet):
        force_vector = Vector(0, 0)
        G = 0.1
        e = 0.0001
        neg_vector = self.pos.s_multiply(-1)
        for i in range(len(planet)):
            if planet[i].name != self.name:
                print(self.name, planet[i].name)
                dist_vec = self.pos.subtract(planet[i].pos)
                dist = dist_vec.magnitude()
                force_vector1 = dist_vec.s_multiply(G * planet[i].m * self.m / (dist + e) ** 3)
                if dist < self.r:
                    force_vector1 = force_vector1.s_multiply(-1)
                force_vector = force_vector.add(force_vector1)
        print('\n')
        return force_vector.s_multiply(-1)

n = int(input('input n:'))
t = 0
dt = 0.001
planet = []
for i in range(n):
    a = rand.random(4)
    p = Planet(rand.randint(1, 5), 0.001, Vector(a[0], a[1]), Vector(a[2], a[3]), str(i))
    planet.append(p)
#p1 = Planet(100, 0.001, Vector(0.1, 0.2), Vector(0.5, 0.75), 'p1')
#p2 = Planet(1, 0.001, Vector(0.2, 0.1), Vector(0.2, 0.5), 'p2')
#p3 = Planet(1, 0.001, Vector(0.2, 0.15), Vector(0.75, 1), 'p3')
#p4 = Planet(1, 0.001, Vector(0.15, 0.15), Vector(0.75, 0.75), 'p4')
#planet = [p1, p2, p3, p4]
if True:
    steps = 2000
    X = []
    Y = []
    for i in range(len(planet)):
        X.append([])
        Y.append([])

        #print(p1.pos.display(), end='  ')
        #print(p2.pos.display(), end=' ')
        #print(p3.pos.display())
    while steps > 0:
        for i in range(len(planet)):
            planet[i].momentum = planet[i].momentum.add(planet[i].force(planet).s_multiply(dt))
            planet[i].pos = planet[i].pos.add((planet[i].momentum.s_multiply(dt)).s_multiply(1/planet[i].m))
            #p1.m = p1.m * (0.999999)
            X[i].append(planet[i].pos.x)
            Y[i].append(planet[i].pos.y)
        t = t + dt
        steps = steps - 1

    for i in range(len(planet)):
        plt.plot(X[i], Y[i], linewidth=0.5)
        plt.scatter(X[i][:1], Y[i][:1], s=30)
    plt.title('N Body Problem (n = ' + str(n) + ')\n')
    plt.show()

