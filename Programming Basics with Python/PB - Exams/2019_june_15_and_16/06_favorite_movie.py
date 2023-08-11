movie_max_points = 0
movie_max_points_name = ""
movie_titles_count = 0

while True:
    command = input()
    if command == "STOP":
        break
    movie_name = command
    movie_points = 0
    for i in range(len(movie_name)):
        movie_points += ord(movie_name[i])
        if ord(movie_name[i]) in range(ord("a"), ord("z") + 1):
            movie_points -= 2 * len(movie_name)
        elif ord(movie_name[i]) in range(ord("A"), ord("Z") + 1):
            movie_points -= len(movie_name)

    if movie_points > movie_max_points:
        movie_max_points = movie_points
        movie_max_points_name = movie_name

    movie_titles_count += 1

    if movie_titles_count == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {movie_max_points_name} "
      f"with {movie_max_points} ASCII sum.")
