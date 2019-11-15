from add import add
from subtraction import subtract
from multiply import multiply
from Division import div





print("<-- Menu -->\n1.Division\n2.Multiplicatoin\n3.Subtraction\n4.Addition")
i = input()
if(i==1):
  x=input("enter x value")
  y=input("enter y value")
  print div(x,y)
elif(i==3):
  x=input("enter x value")
  y=input("enter y value")
  print subtract(x,y)
elif(i==2):
  x=input("enter x value")
  y=input("enter y value")
  print multiply(x,y)
elif(i==4):
  x=input("enter x value")
  y=input("enter y value")
  print add(x,y)
else:
  print("wrong input")
