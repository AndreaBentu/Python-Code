# defining a class called Club which has a name and a list of players.

class Club:
    	def __init__(self, name):
        	self.name = name
        	self.players = []

	def __len(self):
		return len(self.players)

# defining a method to access items in the class via indexing
	def __getitem__(self,i):
		return self.players[i]

# defining a method to return a strig description of the objects' contents
	def __repr__(self):
		return f' These are the players in {self.name}: {self.players}'

# creating an instance of the class Club
Arsenal = Club('Arsenal') 

# adding players to the club
Arsenal.players.append('Rolf') 
Arsenal.players.append('Anne')

print (Arsenal)
