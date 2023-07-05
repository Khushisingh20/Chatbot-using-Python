#userdefined exception

class exception(Exception):
  pass

class MarksOutOfBoundException(exception):
  def _init_(self):
    print("Exception: MarksOutOfBoundException")

name = input("Enter the name of student:L ")
seat = int(input("Enter the seast number: "))
l = []
i = 0
sum=0
total = 0
while i<6:
  try:
    m = int(input("Enter the marks: "))
    if(m<0 or m>100):
      raise MarksOutOfBoundException
    l.append(m)
    sum = sum+m
  except MarksOutOfBoundException:
    print("Enter the correct marks: ")
    continue
  except:
    print("Enter the marks in integer: ")
    continue
  i += 1

print("Student Name: ",name)
print("Student Seat Number: ",seat)
for j in range(6):
  print(l[j])
print(sum)