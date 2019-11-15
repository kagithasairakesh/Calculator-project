import add.py
import subtraction.py
import multiply.py
import Division.py





print("<-- Menu -->\n1.Division\n2.Multiplicatoin\n3.Addition\n4.Subtraction")
i = input()
if(i==1):
  x=input("enter x value")
  y=input("enter y value")
  div(x,y)
elif(i==3):
  x=input("enter x value")
  y=input("enter y value")
  subtr(x,y)
elif(i==2):
  x=input("enter x value")
  y=input("enter y value")
  mult(x,y)
elif(i==4):
  x=input("enter x value")
  y=input("enter y value")
  add(x,y)
else:
  print("wrong input")