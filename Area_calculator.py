"""This program calculates the area of circle and triangle"""

print("The area calculator is starting!")

name = raw_input("Enter C for Circle and T for Triangle: ")

if name == 'C':
  radius = float(raw_input("Enter the radius of the circle: "))
  area = 3.14159 * radius ** 2
  print "The area of your circle is: %f" % area

elif name == 'T':
  base = float(raw_input("Enter the base of the triangle: "))
  height = float(raw_input("Enter the height of the triangle: "))
  area = 0.5 * base * height
  print "The area of your triangle is: %f" % area

else:
  print("Please select C or T")

print "Exiting the calculator!"
