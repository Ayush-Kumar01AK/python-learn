a = int(input("entre marks in physics:"))
b = int(input("entre marks in chemistry:"))
c = int(input("entre marks in maths:"))

t = int(input("total maximum marks in all subjects:"))
total_percentage = ((a+b+c)/t)*100

if(total_percentage>=40 and a>=30 and b>=30 and c>=30):
    print("congratulation you passed the exam with",total_percentage,"percentage")
else:
    print("oops you failed,try better next time",total_percentage)

