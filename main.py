intrusions = int(input("Please enter the number of intrusions: "))
days = int(input("Please enter the number of days tracked: "))
avg_intrusions_per_day = intrusions / days
print(f"Average intrusions per day: {avg_intrusions_per_day:,.2f}")


def range_calculator(avg_intrusions):
    # lower_range, activity_level string

    activity_level = ""
    activity_list = [
        [200, "Critical"],
        [100, "High"],
        [20, "Average"],
        [0, "Low"]
    ]

    for item in activity_list:
        if avg_intrusions >= item[0]:
            activity_level = item[1]
            break

    print(f"Activity level: {activity_level}")


range_calculator(avg_intrusions_per_day)
