# За отговор не се гледат минути, заради което не се зачитат и се използва целочислено делене
# или math.floor (при import-нат math)

number_of_pages = int(input())
pages_read_per_hour = int(input())
number_of_days_required_to_read_the_book = int(input())

number_of_hours = (number_of_pages // pages_read_per_hour) // number_of_days_required_to_read_the_book

print(number_of_hours)