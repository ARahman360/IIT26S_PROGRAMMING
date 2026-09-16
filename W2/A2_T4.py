print("Program starting.")
print("Estimate how many minutes you spent on programming...")

Task1 = int(input("Enter minutes for A1_T1: "))
Task2 = int(input("Enter minutes for A1_T2: "))
Task3 = int(input("Enter minutes for A1_T3: "))
Task4 = int(input("Enter minutes for A1_T4: "))
Task5 = int(input("Enter minutes for A1_T5: "))
Task6 = int(input("Enter minutes for A1_T6: "))
Task7 = int(input("Enter minutes for A1_T7: "))

print("In total you spent {} minutes on programming.".format(Task1 + Task2 + Task3 + Task4 + Task5 + Task6 + Task7))
print("Average per task was {} min and same rounded to the nearest integer {} min.".format((Task1 + Task2 + Task3 + Task4 + Task5 + Task6 + Task7) / 7, round((Task1 + Task2 + Task3 + Task4 + Task5 + Task6 + Task7) / 7)))

print("Program ending.")
