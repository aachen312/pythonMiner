from ys_twitter import TWTR_OAUTH

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = TWTR_OAUTH.twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = TWTR_OAUTH.twitter_api.trends.place(_id=US_WOE_ID)

#print json.dumps(world_trends)
#print
#print json.dumps(us_trends)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print us_trends