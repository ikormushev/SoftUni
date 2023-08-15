movies_num = int(input())

highest_rating = 1.00
highest_rating_name = ""
lowest_rating = 10.00
lowest_rating_name = ""

total_rating = 0

for _ in range(1, movies_num + 1):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rating_name = movie_name
    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_name = movie_name

    total_rating += movie_rating

average_rating = total_rating / movies_num

print(f"{highest_rating_name} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_name} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
