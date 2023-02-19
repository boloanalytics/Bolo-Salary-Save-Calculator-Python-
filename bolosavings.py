name = input('Please tell me your name: ')
monthly_net = int(input('Please tell me your monthly salary: '))
annual_net = (monthly_net * 12)
save_percent = int(input('How many percent of your monthly salary do you want to spread after 12 months of saving: '))
save_value = (save_percent/100 * monthly_net)
remainder_value = (monthly_net - save_value)
save_value_annual = (save_value * 12)
spread_value = (0.40 * save_value_annual)
new_salary_chuck = (spread_value + annual_net)

new_monthly_salary = (new_salary_chuck / 12)

print(f"Hello {name}, your new salary after saving "
      f"{save_percent} percent of your monthly salary of {monthly_net}, will be {new_monthly_salary}")

