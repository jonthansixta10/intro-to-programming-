student = {"name": "Alice", "age": 16, "grade": "A"}
student["grade"] = "A+"
print(student["name"], student["age"], student["grade"])


favorite_movies = [{"title": "Inception", "year": 2010}, {"title": "The Matrix", "year": 1999}, {"title": "gladiator", "year": 2000}]
new_movie = input("Enter the title of the new movie: ")
date = int(input("Enter the release year of the new movie: "))
favorite_movies.append({"title": new_movie, "year": date})
print("Updated list of favorite movies:")
for movie in favorite_movies:
    print(f"{movie['title']} ({movie['year']})")


