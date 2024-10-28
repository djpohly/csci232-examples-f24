# import geometry
# use geometry.rectangle_area(...)
# import geometry as G
# use G.rectangle_area(...)
from geometry import rectangle_area, rectangle_perimeter

length = input("What is the length? ")
width = input("What is the width? ")

l = float(length)
w = float(width)

area = rectangle_area(l, w)
per = rectangle_perimeter(l, w)

print("You need " + str(area) + " square feet of carpet")
print("You need " + str(per) + " feet of wallpaper")
