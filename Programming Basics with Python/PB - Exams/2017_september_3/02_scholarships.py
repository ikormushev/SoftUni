from math import floor

salary_bgn = float(input())
average_score = float(input())
min_wage = float(input())

social_scholarship = min_wage * 0.35
high_score_scholarship = average_score * 25

if salary_bgn < min_wage and average_score > 4.5 and social_scholarship > high_score_scholarship:
    print("You get a Social scholarship " + str(floor(social_scholarship)) + " BGN")

elif average_score >= 5.5 and high_score_scholarship >= social_scholarship:
    print("You get a scholarship for excellent results " + str(floor(high_score_scholarship)) + " BGN")

else:
    print("You cannot get a scholarship!")
