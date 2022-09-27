age = input("What is your current age?")

convert_age = int(age)

#Data reference 1 year
days_year = 365
weeks_year = 52
month_year = 12

#Data Reference 90yo
days_90yo = days_year * 90
weeks_90yo = weeks_year * 90
month_90yo = month_year * 90

#main
day_left = days_90yo - (convert_age * days_year)
week_left = weeks_90yo - (convert_age * weeks_year)
month_left = month_90yo - (convert_age * month_year)

print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left. ")

