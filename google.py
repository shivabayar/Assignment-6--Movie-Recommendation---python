def calculateAverage(movies):
    
    for movie in movies.keys():
        movies.get(movie)["averageRating"] = float(movies.get(movie)["totalRating"])/float(movies.get(movie)["ratingCount"])
        
    return movies

def findMax(filteredMap):
    
    filteredMapKeys = filteredMap.keys()
    maxId = int(filteredMapKeys[0])
    filteredMapKeys.remove(maxId)
    maxRating = float(filteredMap.get(maxId)["averageRating"])
    maxRatingCount =  filteredMap.get(maxId)["ratingCount"]
     
    for Map in filteredMap.keys():
        tempId = int(Map)
        tempMaxRating = float(filteredMap.get(tempId)["averageRating"])
        tempMaxRatingCount = filteredMap.get(tempId)["ratingCount"]
        if tempMaxRating > maxRating and tempMaxRatingCount > maxRatingCount:
            maxRating = tempMaxRating
            maxId = tempId
            maxRatingCount = tempMaxRatingCount
            
    return maxId
    
def topMovieByRating(movies):
    
    filteredMap = {}
    
    for movie in movies.keys():
        filteredMap[movie] = {}
        filteredMap[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
        filteredMap[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
    
    return findMax(movies)

def topMovieByGenre(movies,genre):
    
    filteredMovies = {}
    
    for movie in movies.keys():
        movie = int(movie)
        #find the particular genre in individual movie
        if genre in movies.get(movie)["genre"]:
            filteredMovies[movie] = {}
            filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
            filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
            
    return findMax(filteredMovies)


def topMovieByYear(movies,year):
    filteredMovies = {}
    
    for movie in movies.keys():
        movie = int(movie)
        
        if(movies.get(movie)["year"] == year):
            filteredMovies[movie] = {}
            filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
            filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
            
    return findMax(filteredMovies)

