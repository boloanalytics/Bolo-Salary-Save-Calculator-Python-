name = input('Please tell me your name: ')
monthly_net = int(input('Please tell me your monthly salary: '))
annual_net = (monthly_net * 12)
save_percent = int(input('How many percent of your monthly salary do you want to save across 12 months: '))
save_value = (save_percent/100 * monthly_net)
remainder_value = (monthly_net - save_value)
save_value_annual = (save_value * 12)
spread_value = (0.40 * save_value_annual)
new_salary_chuck = (spread_value + annual_net)

new_monthly_salary = (new_salary_chuck / 12)

print(f"Hello {name}, the value of your monthly spend will be {0.40 * monthly_net}")

print(f"The value of your monthly savings will be {0.60 * monthly_net}")

print(f"The value of your new salary in a new 12-months calendar after saving "
      f"{save_percent} percent of your monthly salary of {monthly_net}, will be {new_monthly_salary}, "
      f"and this amount will be the start of a new calendar month should you intend to continue "
      f"the same process for the new 12-months cycle!")

print(f"Hence, the total savings left in your 12-months savings, "
      f"after the spread deductions will be {round(.60 * save_value_annual,2)}")

