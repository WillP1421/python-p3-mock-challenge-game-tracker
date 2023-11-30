class Game:
    def __init__(self, title):
        self.title = title

    def set_title(self, title):
        has_title = hasattr(self, 'title')
        if has_title:
            return
        elif isinstance(title, str) and title:
            self._title = title
        else:
            print("Title must be a non-empty string.")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        return sum([result.score for result in self.results() if result.player == player]) / len(self.results())

class Player:
    all = []
    def __init__(self, username):
        self.username = username
    @property 
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username
    def results(self):
        return [result for result in Result.all if result.player == self]
    def games_played(self):
        return list({result.game for result in self.results()})
                        
                
    def played_game(self, game):
        return game in self.games_played()
                
    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])
class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be of type Player.")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be of type Game.")
    
    
    
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score