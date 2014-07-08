import readFile
import google

if __name__ == "__main__":    
    movies = readFile.readMovieAndParse("movie.data") #dictrionary of movies
    users = readFile.readUserFile("user.data")
    readFile.readRatings("ratings.data",movies,users)
    movies = google.calculateAverage(movies)
    print movies.get(google.topMovieByRating(movies))["movieName"]
    print movies.get(google.topMovieByGenre(movies, "Thriller"))["movieName"]
    print movies.get(google.topMovieByYear(movies, 1995))["movieName"]
    if google.topMovieByYearAndGenre(movies,1988,"Action") != 0:
        print movies.get(google.topMovieByYearAndGenre(movies,1988,"Action"))["movieName"]
        
    print movies.get(google.mostWatchedMovie(movies))["movieName"]
    print users.get(google.mostActiveUser(users))
        
#     print movies.get(181)