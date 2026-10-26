from recommender import recommended_movies

print("Welcome to Movie Recommendation System !")

movie_name = input("Enter the movie name: ")
number_of_recommendations = int(input("Enter the number of recommendations you want: "))

print(f"Top {number_of_recommendations} recommended movies based on your input:")
print(recommended_movies(movie_name, number_of_recommendations))