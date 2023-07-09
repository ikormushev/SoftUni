from math import ceil

steps_number = int(input())
dancers_number = int(input())
days = int(input())

required_steps_per_day = steps_number / days
percent_steps_per_day = ceil((required_steps_per_day / steps_number) * 100)
percent_steps_per_dancer = percent_steps_per_day / dancers_number
wanted_steps_per_day = (percent_steps_per_day * required_steps_per_day) / 100

if wanted_steps_per_day <= (0.13 * required_steps_per_day):
    print("Yes, they will succeed in that goal! " + '{0:.2f}'.format(percent_steps_per_dancer) + "%.")
else:
    print("No, They will not succeed in that goal! "
          "Required " + '{0:.2f}'.format(percent_steps_per_dancer) + "% steps to be learned per day.")
