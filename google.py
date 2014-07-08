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
    
    filteredMovies = {}
    
    for movie in movies.keys():
        filteredMovies[movie] = {}
        filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
        filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
#     print movies.get(144)["ratingCount"] = movies.get(movie)["ratingCount"]
    
    if len(filteredMovies) > 0:
        return findMax(filteredMovies)
    else :
        return 0

def topMovieByGenre(movies,genre):
    
    filteredMovies = {}
    
    for movie in movies.keys():
        movie = int(movie)
        #find the particular genre in individual movie
        if genre in movies.get(movie)["genre"]:
            filteredMovies[movie] = {}
            filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
            filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
            
    if len(filteredMovies) > 0:
        return findMax(filteredMovies)
    else :
        return 0


def topMovieByYear(movies,year):
    filteredMovies = {}
    
    for movie in movies.keys():
        movie = int(movie)
        
        if(movies.get(movie)["year"] == year):
            filteredMovies[movie] = {}
            filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
            filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
            
    if len(filteredMovies) > 0:
        return findMax(filteredMovies)
    else :
        return 0

def topMovieByYearAndGenre(movies,year,genre):
    filteredMovies = {}
    
    for movie in movies.keys():
        movie= int(movie)
        
        if(movies.get(movie)["year"] == year and genre in movies.get(movie)["genre"]):
            filteredMovies[movie] = {}
            filteredMovies[movie]["averageRating"] = float(movies.get(movie)["averageRating"])
            filteredMovies[movie]["ratingCount"] = movies.get(movie)["ratingCount"]
      
#     print filteredMovies   
    if len(filteredMovies) > 0:
        return findMax(filteredMovies)
    else :
        return 0
    
def findMaximum(filteredMap):
    filteredMapKeys = filteredMap.keys()
    maxId = int(filteredMapKeys[0])
    filteredMapKeys.remove(maxId)
    maxRatingCount =  filteredMap.get(maxId)
     
    for Map in filteredMap.keys():
        tempId = int(Map)
        tempMaxRatingCount = filteredMap.get(tempId)
        if  tempMaxRatingCount > maxRatingCount:
            maxId = tempId
            maxRatingCount = tempMaxRatingCount
            
    return maxId

def mostWatchedMovie(movies):
    
    filteredMovies = {}
    
    for movie in movies.keys():
        movie = int(movie)
        filteredMovies[movie] = movies.get(movie)["ratingCount"]
        
    return findMaximum(filteredMovies)

def mostActiveUser(users):
    filteredUsers = {}
    
    for user in users.keys():
        user = int(user)
        filteredUsers[user] = users.get(user)["numberOfTimesRated"]
        
    return findMaximum(filteredUsers)