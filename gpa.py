print("Program To Calaculate GPA : ************* : ")
n = int(input("Enter Number Of Subject : "))
print("Enter One Subject, press enter to enter another subject")
subject = [ int(input()) for i in range(n)]
w = sum(subject)
average = w/n
if average>=80:
    print("First Class")
elif average>=60 and average<80:
    print("Second Class")
else:
   print("Third Class")
print("Your Average Is ", average)
