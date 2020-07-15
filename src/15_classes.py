# Make a class LatLon that can be passed parameters `lat` and `lon` to the constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon): # self == this; (lat, lon) == parameters (before they are defined)
        self.lat = lat # argument 1
        self.lon = lon # argument 2
        
latlon = LatLon(32, -118)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): # grabbing parent LatLon
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon) # similar to react's super - class components
        self.name = name
    
    def __str__(self): # human readable 
        # return '%s, %.2f, %.4f' % (self.name, self.lat, self.lon) # regex == all to be string
        return f'{"name: " + str(self.name)}, {"lat: " + str(self.lat)}, {"lon: " + str(self.lon)}'
        
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.size = size
        self.difficulty = difficulty
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
    def __str__(self):
        return f'{"name: " + str(self.name)}, {"diff: " + str(self.difficulty)}, {"size: " + str(self.size)}, {"lat: " + str(self.lat)}, {"lon: " + str(self.lon)} '

# YOUR CODE HERE
new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method 
# print(waypoint)
print(str(new_waypoint))


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
new_geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
# print(geocache)
print(str(new_geocache))
