import re

def readTheFile(fileName):
    File = open(fileName)
    lines = File.readlines()
    
    return lines

    
def readMovieAndParse(fileName):
    
    lines = readTheFile(fileName)    
    genreLines = readTheFile("genre.data")
    genre = {}
    for line in genreLines:
        line = line.split("|")
        genre[int(line[1])] = line[0]
        
    movies = {}
    
    for line in lines:
        line = line.split("|")
        line.remove("")
        movieId = int(line[0])
        movies[movieId] = {}
        movies[movieId]["movieName"] = line[1]
        a = re.search("(\d+)-(\w+)-(\d+)",str(line[2]))
        if a != None:
            year = a.group(3)
        else:
            year = 0000
        movies[movieId]["year"] = int(year)
        movies[movieId]["genre"] = list("")
        movies[movieId]["totalRating"] = 0
        movies[movieId]["ratingCount"] = 0
        movies[movieId]["averageRating"] = float(0.0)
        #finding out which genre the movie belongs by checking it genre dict
        i = 4
        while(i < 23):
            if(int(line[i]) == 1):
                movies[movieId]["genre"].append(genre.get(i - 4)) 
            i += 1

    return movies  # returns map of movies

def readUserFile(fileName):
    lines = readTheFile(fileName)
    users = {}
    
    for line in lines:
        line = line.split("|")
        users[int(line[0])] = {"age":line[1], "gender":line[2], "profession":line[3], 
                         "pincode":line[4], "numberOfTimesRated":0}
    return users

def readRatings(fileName, movies, users):
    
    lines = readTheFile(fileName)
    
    for line in lines:
        line = line.split("\t")
        userId = int(line[0])
        movieId = int(line[1])
        rating = int(line[2])
        movies.get(movieId)["ratingCount"] += 1
        movies.get(movieId)["totalRating"] += rating
        users.get(userId)["numberOfTimesRated"]+= 1