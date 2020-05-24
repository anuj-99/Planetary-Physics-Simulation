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

    def force(self, planet1, planet2):
        G = 0.1
        neg_vector = self.pos.s_multiply(-1)
        dist_vec1 = self.pos.subtract(planet1.pos)
        dist1 = dist_vec1.magnitude()
        force_vector1 = dist_vec1.s_multiply(G * planet1.m * self.m / dist1 ** 3)
        dist_vec2 = self.pos.subtract(planet2.pos)
        dist2 = dist_vec2.magnitude()
        force_vector2 = dist_vec2.s_multiply(G * planet2.m * self.m / dist2 ** 3)
        force_vector = force_vector1.add(force_vector2)
        return force_vector.s_multiply(-1)


t = 0
dt = 0.00001
p1 = Planet(0.5, 3, Vector(0.1, 0.2), Vector(0.5, 0.75))
p2 = Planet(2, 3, Vector(0.2, 0.1), Vector(1.5, 1))
p3 = Planet(1, 2, Vector(0.4, 0.4), Vector(0.75, 1))
steps = 80000
ind = steps
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
while steps > 0:
    print(p1.pos.display(), end='  ')
    print(p2.pos.display(), end=' ')
    print(p3.pos.display())
    p1.momentum = p1.momentum.add(p1.force(p2, p3).s_multiply(dt))
    p2.momentum = p2.momentum.add(p2.force(p1, p3).s_multiply(dt))
    p3.momentum = p3.momentum.add(p3.force(p1, p2).s_multiply(dt))
    p1.pos = p1.pos.add((p1.momentum.s_multiply(dt)).s_multiply(1/p1.m))
    p2.pos = p2.pos.add((p2.momentum.s_multiply(dt)).s_multiply(1/p2.m))
    p3.pos = p3.pos.add((p3.momentum.s_multiply(dt)).s_multiply(1/p3.m))
    x1.append(p1.pos.x)
    y1.append(p1.pos.y)
    x2.append(p2.pos.x)
    y2.append(p2.pos.y)
    x3.append(p3.pos.x)
    y3.append(p3.pos.y)
    t = t + dt
    steps = steps - 1
plt.plot(x1, y1, color='r', linewidth=0.5)
plt.plot(x2, y2, color='y', linewidth=0.5)
plt.plot(x3, y3, color='g', linewidth=0.5)
plt.scatter(x1[:1], y1[:1], s=20, color='b')
plt.scatter(x2[:1], y2[:1], s=20, color='b')
plt.scatter(x3[:1], y3[:1], s=20, color='b')
plt.scatter(x1[ind - 1], y1[ind - 1], s=20, color='g')
plt.scatter(x2[ind - 1], y2[ind - 1], s=20, color='g')
plt.scatter(x3[ind - 1], y3[ind - 1], s=20, color='g')
plt.show()
