import readFile
import google

if __name__ == "__main__":    
    movies = readFile.readMovieAndParse("movie.data") #dictrionary of movies
    users = readFile.readUserFile("user.data")
    readFile.readRatings("ratings.data",movies,users)
    movies = google.calculateAverage(movies)
    print movies.get(google.topMovieByRating(movies))["movieName"]
#     print google.topMovieByRating(movies)
    print movies.get(google.topMovieByGenre(movies, "Thriller"))["movieName"]
    print movies.get(google.topMovieByYear(movies, 1971))["movieName"]
