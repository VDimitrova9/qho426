print("Please choose an option:\n\n1 - Nice message\n2 - Area of a rectangle\n3 - Area of a triangle\n4 - Multiplication table")

option = int(input("\n Enter option:"))

if option ==1:
  print("You don't smell so bad today!")
elif option == 2:
  l = float(input("Enter the lenght of the rectangle:"))

  w = float(input("Enter the height of the rectangle:"))
  area = l*w
  print("Area of this rectangle is {:.2f}".format(l*w))
elif option ==3:
  b = float(input("Enter the base of the triangle:"))

  h = float(input("Enter the height of the triangle:"))
  print("Area of this triangle is {:.2f}".format(b*h/2))
elif option == 4:
  pass
else:
  print("Go to Specsavers")
