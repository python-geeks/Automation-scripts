import sys
import imdb

imdb_object = imdb.IMDb()

if len(sys.argv) != 2:
    print("Please provide movie name in proper format!!!")
    sys.exit()

movie_name = sys.argv[1].replace('_', ' ')

try:
    search_result = imdb_object.search_movie(movie_name, 1)
    movie_data = search_result[0].__dict__
    vote_details = imdb_object.get_movie_vote_details(movie_data["movieID"])
    movie_rating_stats = vote_details["data"]["demographics"]["imdb users"]
    print("Rating: %s, based on %s votes" % (movie_rating_stats["rating"], movie_rating_stats["votes"]))

except KeyError:
    print("Movie ratings data is not available")
    sys.exit()
