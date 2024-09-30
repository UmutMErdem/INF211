class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def get_name(self):
        return f'{self.name} {self.lastname}'
    def __str__(self):
        return f'{self.name} {self.lastname}'
    def __lt__(self, other):
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

class Player(Person):
    counter = 0
    def __init__(self, name, lastname):
        from random import randint
        super().__init__(name, lastname)
        self.sp = randint(4, 8)
        self.liste = []
        self.flg = False
        self.flgr = False
        self.team = ""
    def reset(self):
        self.flgr = True
        self.liste = []
    def get_id(self):
        if not self.flg:
            self.id = Player.counter
            Player.counter += 1
            self.flg = True
        elif self.flgr:
            self.id = 0
        return self.id
    def get_power(self):
        return self.sp
    def set_team(self, t):
        self.team = t
    def get_team(self):
        return self.team
    def add_to_points(self, x):
        self.liste.append(x)
        return sum(self.liste)
    def get_points_detailed(self):
        return self.liste
    def get_points(self):
        return sum(self.liste)
    def __lt__(self, other):
        if self.liste == other.liste:
            return super().__lt__(other)
        return self.liste < other.liste

class Manager(Person):
    counter = 0
    def __init__(self, name, lastname):
        super().__init__(name, lastname)
        self.mp = []
        self.flg = False
        self.flgr = False
        self.team = ""
    def reset(self):
        self.flgr = True
        self.mp = []
    def get_id(self):
        if not self.flg:
            self.id = Manager.counter
            Manager.counter += 1
            self.flg = True
        elif self.flgr:
            self.id = 0
        return self.id
    def set_team(self, t):
        self.team = t
    def get_team(self):
         return self.team
    def get_influence_detailed(self):
        return self.mp
    def get_influence(self):
        return sum(self.mp)
    def __lt__(self, other):
        if self.mp == other.mp:
            return super().__lt__(other)
        return self.mp < other.mp

class Team:
    counter = 0
    def __init__(self, teamname, manager, players):
        self.teamname = teamname
        self.manager = manager
        self.manager.set_team(self.teamname)
        self.players = players
        self.w, self.l = [], []
        self.week = []
        self.fix = []
        self.flg = False
        self.flgr = False
    def reset(self):
        self.flgr = True
        self.manager.mp = []
        for i in self.players: i.liste = []
        self.fix = []
    def get_id(self):
        if not self.flg:
            self.id = Team.counter
            Team.counter += 1
            self.flg = True
        elif self.flgr:
            self.id = 0
        return self.id
    def get_name(self):
        return self.teamname
    def get_roster(self):
        return self.players
    def get_manager(self):
        return self.manager.get_name()
    def add_to_fixture(self, m):
        self.fix.append(m)
    def get_fixture(self):
        return self.fix
    def add_results(self, s):
        self.w.append(["add", s[0]])
        self.l.append(["add", s[1]])
    def get_scored(self):
        return sum([i[1] for i in self.w])
    def get_conceded(self):
        return sum([i[1] for i in self.l])
    def get_wins(self):
        return len(self.w)
    def get_losses(self):
        return len(self.l)
    def __str__(self):
        return self.get_name()
    def __lt__(self, other):
        for i in self.week:
            if i == other:
                for j in self.w:
                    if j[0] == self.week.index(i): return False
                for j in self.l:
                    if j[0] == self.week.index(i): return True
                if self.get_scored() - self.get_conceded() > other.get_scored() - other.get_conceded(): return False
                else: return True

class Match:
    def __init__(self, home_team, away_team, week_no):
        self.home_team = home_team
        self.away_team = away_team
        self.week_no = week_no
        self.flag = False
    def is_played(self):
        return self.flag
    def play(self):
        from random import randint
        self.flag = True
        self.home_manager_point, self.away_manager_point = randint(-10, 10), randint(-10, 10)
        self.home_score, self.away_score = self.home_manager_point, self.away_manager_point
        liste = []
        for i in range(4):
            if not liste:
                liste.append([j.get_power() for j in self.home_team.get_roster()])
                liste.append([j.get_power() for j in self.away_team.get_roster()])
            for j in range(len(liste)):
                for k in range(len(liste[j])): liste[j][k] += randint(-5, 5)
        self.home_score += sum(liste[0])
        self.away_score += sum(liste[1])
        if self.home_score == self.away_score:
            for j in range(len(liste)):
                for k in range(len(liste[j])):
                    a = randint(-5, 5)
                    liste[j][k] += a
                    if j == 0: self.home_score += a
                    else: self.away_score += a
        for i, j in enumerate(self.home_team.players, 0): j.liste.append(liste[0][i])
        for i, j in enumerate(self.away_team.players, 0): j.liste.append(liste[1][i])
        self.home_team.manager.mp.append(self.home_manager_point)
        self.away_team.manager.mp.append(self.away_manager_point)
        self.home_team.week.append(self.away_team)
        self.away_team.week.append(self.home_team)
        if self.home_score > self.away_score:
            self.home_team.w.append([self.week_no, self.home_score])
            self.away_team.l.append([self.week_no, self.away_score])
        elif self.away_score > self.home_score:
            self.away_team.w.append([self.week_no, self.away_score])
            self.home_team.l.append([self.week_no, self.home_score])
    def get_match_score(self):
        return (self.home_score, self.away_score)
    def get_teams(self):
        return (self.home_team, self.away_team)
    def get_home_team(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team
    def get_winner(self):
         if self.flag:
            if self.home_score > self.away_score:
                return self.home_team
            elif self.away_score > self.home_score:
                return self.away_team
         return None
    def __str__(self):
        if self.flag: return f'{self.home_team} ({self.home_score}) vs. ({self.away_score}) {self.away_team}'
        else: return f'{self.home_team} vs. {self.away_team}'

class Season:
    def __init__(self, teams_file, managers_file, players_file):
        from random import randint, shuffle
        self.thng, counter = [], 1
        self.teams, self.managers, self.players = [], [], []
        for i in [teams_file, managers_file, players_file]:
            with open(i, "r") as file:
                for j in file.readlines():
                    self.thng.append(j.strip())
            if counter == 1: self.teams = self.thng[::]
            elif counter == 2: self.managers = [k.split() for k in self.thng[::]]
            elif counter == 3: self.players = [k.split() for k in self.thng[::]]
            self.thng.clear()
            counter += 1
        counter = len(self.players)
        for i in range(len(self.teams)):
            plyrs = []
            for j in range(5):
                g = randint(0, counter - 1)
                plyrs.append(Player(self.players[g][0], self.players[g][1]))
                self.players.pop(g)
                counter -= 1
            self.thng.append(Team(self.teams[i], Manager(self.managers[i][0], self.managers[i][1]), plyrs))
        shuffle(self.thng)
        self.w = 0
        self.build_fixture()
    def reset(self):
        pass
    def build_fixture(self):
        self.fixtr = []
        counter = 1
        for i in range(2):
            liste = self.thng.copy()
            for j in range(len(self.teams)-1):
                if i == 0:
                    self.fixtr.append([Match(liste[k], liste[len(liste)-1-k], week_no=counter) for k in range(len(self.teams)//2)])
                else:
                    self.fixtr.append([Match(liste[len(liste)-1-k], liste[k], week_no=counter) for k in range(len(self.teams)//2)])
                liste.insert(1, liste.pop())
                counter += 1
    def get_week_fixture(self, week_no):
        return self.fixtr[week_no]
    def get_week_no(self):
        return self.w
    def play_week(self):
        if self.w < 2*len(self.teams) - 2:
            for i in self.fixtr[self.w]:
                i.play()
            self.w += 1
    def get_players(self):
        return self.players1
    def get_managers(self):
        return self.managers1
    def get_teams(self):
        return self.thng
    def get_season_length(self):
        return 2*len(self.teams)-2
    def get_best_player(self):
        b, a = None, 0
        self.players1 = [j for i in self.thng for j in i.players]
        for i in self.players1:
            if i.get_points() > a:
                a, b = i.get_points(), i
        if b != None: return b.get_name()
    def get_best_manager(self):
        b, a = None, 0
        self.managers1 = [i.manager for i in self.thng]
        for i in self.managers1:
            if i.get_influence() > a:
                a, b = i.get_influence(), i
        if b != None: return b.get_name()
    def get_most_scoring_team(self):
        a, b = 0, None
        for i in self.thng:
            if i.get_scored() > a:
                a, b = i.get_scored(), i
        if b != None: return b.get_name()
    def get_champion(self):
        if self.get_week_no() == self.get_season_length():
            a, b = 0, None
            for i in self.thng:
                if i.get_wins() > a:
                    a, b = i.get_wins(), i
            return b.get_name()
        
if __name__ == "__main__":

    teams_file = 'teams.txt'
    managers_file = 'managers.txt'
    players_file = 'players.txt'

    # Create a season
    season21 = Season(teams_file, managers_file, players_file)

    # Play the matches
    for i in range(season21.get_season_length()):
        season21.play_week()

    # Get season statistics
    print("Champion is:", season21.get_champion() )
    print("Most scoring team is:", season21.get_most_scoring_team() )
    print("Best player is:", season21.get_best_player() )
    print("Best manager is:", season21.get_best_manager() )