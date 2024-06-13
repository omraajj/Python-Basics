x = 6 #Integer
Name = "John" #String
a = 5.2 #Float
b = True #Boolean
c = None #Null
print(Name,x,a,b,c)
# Variable do not need to be Declared with any particular type
# Python is Dynamically Typed

name = "Omraj"
print(type(name))

standard = "10th"
print(type(standard))

rollNumber = 21
print(type(rollNumber))

percentage = 51.5
print(type(percentage))

isStudent = True
print(type(isStudent))

# Adding with Simple Commaa
print("My Name is", name,"and My Roll No. is", rollNumber)

#Concatenate with name(Str)
print("My Name is "+ name +" and My Roll No. is", rollNumber)

#Can't Concatenate with other Data Type Like (Integer, Float, etc)
#print("My Name is "+ name +" and My Roll No. is"+ rollNumber)

#Print Expression
print("My Percentage is ",percentage + 1.2,"and My Roll Number is", rollNumber - 1,
      "My Percentage are", percentage/2.0, "My Class is", percentage*2)

#Print with Seperation
print(name,rollNumber,percentage,sep="    ")
