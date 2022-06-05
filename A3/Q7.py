shapes={"Circle":0, "Ellipse":0, "Rhombus":0, "Shape":0}
class Shape:
    # initializing iD to 1 for the 1st obj created
    ID = 1

    def __init__(self):
        self.ID = Shape.ID
        Shape.ID += 1  # creating ID each time we create an obj

    def perimeter(self):
        return 'Undefined'

    def area(self):
        return 'Undefined'

    def printshape(self, name):
        return print("The shape is: ", self.__class__.__name__, " \n The ID is: ", self.ID,
                     "\n The area is: ", self.area(), "\n The parameter is: ", self.perimeter())

class Circle(Shape):
    radius = 0.0

    def __init__(self, radius):
        super().__init__()
        self.radius = float(radius)

    def perimeter(self):
        return round(2.0 * 3.14 * self.radius, 2)

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)


class Ellipse(Shape):
    a = 0.0
    b = 0.0

    def __init__(self, a, b):
        super().__init__()
        # greater value of a and b is the semi-major axis and lesser value is the semi-minor axis
        if a > b:
            self.a = float(a)
            self.b = float(b)
        else:
            self.b = float(a)
            self.a = float(b)

    def area(self):
        return round(3.14 * self.a * self.b, 2)

    # calculate the linear eccentricity of the ellipse
    def eccentricity(self):
        # try to calculate the linear eccentricity,
        try:
            return round((self.a ** 2 - self.b ** 2) ** (1 / 2), 2)
        # if the calculation fails, return None
        except:
            return None


class Rhombus(Shape):
    d1 = 0
    d2 = 0

    def __init__(self, d1, d2):
        super().__init__()
        # initializing the two diagonals
        self.d1 = float(d1)
        self.d2 = float(d2)

    def perimeter(self):
        return round(2 * ((self.d1 ** 2 + self.d2 ** 2) ** (1 / 2)), 2)

    def area(self):
        return round((self.d1 * self.d2) / 2, 2)

    def inradius(self):
        try:
            return round((self.d1 * self.d2) / self.perimeter(), 2)
        # if the calculation fails, return None
        except:
            return None


class main:
    crcounter = 0
    elcounter = 0
    rhcounter = 0
    count = 0
    f = open("input", "r")
    inputArr = f.readlines()
    for line in inputArr:
        strArr = line.split()
        # for line in inputArr:
        if (strArr[0].lower() == 'shape'):
            if (len(strArr) > 1):
                print('Error: invalid Shape')
                sh = Shape()
                pass
            else:
                sh = Shape()
            print(sh.ID, '. Shape, perimeter:', sh.perimeter(), ', area:', sh.area())

        elif (strArr[0].lower() == 'circle'):
            if (len(strArr) > 2 or len(strArr) < 2 or int(strArr[1]) < 0):
                print('Error: invalid Circle')
                cr = Circle(0)
                pass
            else:
                cr = Circle(strArr[1])
            shapes["Circle"]=shapes["Circle"]+1
            print(cr.ID, '. Circle, perimeter:', cr.perimeter(), ', area: ', cr.area())

        elif (strArr[0].lower() == 'ellipse'):
            if (len(strArr) > 3 or len(strArr) < 3 or int(strArr[1]) < 0 or int(strArr[2]) < 0):
                print('Error: invalid Ellipse')
                el = Ellipse(0, 0)
                pass
            else:
                el = Ellipse(strArr[1], strArr[2])
            shapes["Ellipse"]=shapes["Ellipse"]+1
            print(el.ID, '. Ellipse, perimeter:', el.perimeter(), ', area: ', el.area(), ', linear eccentricity: ',
                  el.eccentricity())

        elif (strArr[0].lower() == 'rhombus'):
            if (len(strArr) > 3 or len(strArr) < 3 or int(strArr[1]) < 0 or int(strArr[2]) < 0):
                print('Error: invalid Rhombus')
                rh = Rhombus(0, 0)
                pass
            else:
                rh = Rhombus(strArr[1], strArr[2])
            shapes["Rhombus"]=shapes["Rhombus"]+1
            print(rh.ID, '. Rhombus, perimeter:', rh.perimeter(), ', area: ', rh.area(), ', in-radius: ', rh.inradius())
        shapes["Shape"]=shapes["Shape"]+1

    print('Statistics: \n   Circle(s): ', shapes["Circle"], '\n   Ellipse(s): ', shapes["Ellipse"], '\n   Rhombus(es): ', shapes["Rhombus"],
          '\n      -- \n    Shape(s): ', shapes["Shape"])
