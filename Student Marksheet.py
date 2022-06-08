 # python program to print the student mark sheet

Subject =["Math", "Science","History"]
Marks =[]

name = input("Enter the Name of Sutdent ")
fname = input("Enter the father name")
standard=input("Enter the Standard ")
rnumber = input("Enter the Roll No ")
college = input("Enter your college Name ")

for x in Subject:
    a=int(input("Enter the marks "+x))
    Marks.append(a)


print("\n\n\t\t********************** YOUR RESULT *********************\n\n")

print("\t\tCOLLEGE: ", college)
print("\n\t\tNAME:        ", name, "\t\tFATHER NAME: ", fname)
print("\n\t\tROLL NUMBER: ", rnumber)
print("\n\t\t SUBJECTS             Marks")
for (x, y, z) in zip(Subjest, Marks):
    print("\n\t\t", x, "             ", y, ")

 