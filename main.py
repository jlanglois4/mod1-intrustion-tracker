intrusions = int(input("Please enter the number of intrusions: "))
days = int(input("Please enter the number of days tracked: "))
avg_intrusions_per_day = (intrusions / days)
print(f"Average intrusions per day: {avg_intrusions_per_day:,.2f}")

low_activity_upper_range = 20
average_activity_upper_range = 100
high_activity_upper_range = 200

low_activity = "Low"
average_activity = "Average"
high_activity = "High"
critical_activity = "Critical"
activity_level = ""

if avg_intrusions_per_day >= high_activity_upper_range:
    activity_level = critical_activity
elif avg_intrusions_per_day >= average_activity_upper_range:
    activity_level = high_activity
elif avg_intrusions_per_day >= low_activity_upper_range:
    activity_level = average_activity
else:
    activity_level = low_activity

print(f"Activity level: {activity_level}")
