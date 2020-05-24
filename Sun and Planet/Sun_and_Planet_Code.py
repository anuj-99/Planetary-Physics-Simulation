import math
from matplotlib import pyplot as plt


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
    def __init__(self, mass, rad, pos, vel):
        self.m = mass
        self.r = rad
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.vel = vel
        self.momentum =  vel.s_multiply(self.m)

    def force(self, planet):
        G = 0.1
        neg_vector = self.pos.s_multiply(-1)
        dist_vec = self.pos.subtract(planet.pos)
        dist = dist_vec.magnitude()
        force_vector = dist_vec.s_multiply(G * planet.m * self.m / dist ** 3)
        return force_vector.s_multiply(-1)


t = 0
dt = 0.00001
p1 = Planet(0.5, 3, Vector(0.1, 0.2), Vector(0.5, 0.75))
p2 = Planet(2, 3, Vector(0.2, 0.1), Vector(1.5, 1))
steps = 80000
index = steps
x1 = []
y1 = []
x2 = []
y2 = []
while steps > 0:
    print(p1.pos.display(), end='  ')
    print(p2.pos.display())
    p1.momentum = p1.momentum.add(p1.force(p2).s_multiply(dt))
    p1.pos = p1.pos.add((p1.momentum.s_multiply(dt)).s_multiply(1/p1.m))
    x1.append(p1.pos.x)
    y1.append(p1.pos.y)
    x2.append(p2.pos.x)
    y2.append(p2.pos.y)
    t = t + dt
    steps = steps - 1
plt.plot(x1, y1, color='r', linewidth=0.5, label=('P1 (relative mass ' + str(p1.m) + ')'))
plt.scatter(x2, y2, s=50, color='y', label=('P2 (relative mass ' + str(p2.m) + ')'))
plt.scatter(x1[:1], y1[:1], s=50, color='b')
plt.scatter(x1[index-1], y1[index-1], s=50, color='g')
plt.legend()
plt.show()
