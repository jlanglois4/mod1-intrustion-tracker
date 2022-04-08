intrusions = int(input("Please enter the number of intrusions: "))
days = int(input("Please enter the number of days tracked: "))
average_intrusions_per_day = intrusions / days
print("Average intrusions per day:", average_intrusions_per_day.__round__(2))
