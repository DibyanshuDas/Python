print("Database :-\n")
N = input('Enter your name :-\n')
C = input('Enter your class :-\n')
Ph = input('Enter your Phone Number :-\n')


f = open("database.txt" , "a")
f.write("  ||  ")
f.write(N)
f.write("  ||  ")
f.write(C)
f.write("  ||  ")
f.write(Ph)
f.write("  ||  \n")
f.close()


k = input("Press Enter to exit")
print("k")
