from __future__ import division

class Lineup:
    def __init__(self, players):
        self.players = players

    def __str__(self):
        res = '\n'.join([str(index + 1) + ". " + str(player) for index, player in enumerate(self.players)])
        res += '\nFantasy Points ' + str(sum(player.fppg for player in self.players))
        res += '\nSalary ' + str(sum(player.salary for player in self.players))
        return res

    @property
    def lineup(self):
        return self.players

    @property
    def fantasy_points_projection(self):
        return sum(player.fppg for player in self.players)

    @property
    def salary_costs(self):
        return sum(player.salary for player in self.players)

class Player(object):
    def __init__(self, id,  first_name, last_name, positions, team, salary, fppg, is_injured=False, max_exposure=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.positions = positions
        self.team = team.upper()
        self.salary = salary
        self.fppg = fppg
        self.is_injured = is_injured
        self._max_exposure = None
        self.max_exposure = max_exposure

    def __str__(self):
        return "{}{}{}{}{}".format(
            "{:<30}".format(self.full_name),
            "{:<5}".format('/'.join(self.positions)),
            "{:<15}".format(self.team),
            "{:<8}".format(str(round(self.fppg, 3))),
            "{:<10}".format(str(self.salary) + '$')
        )

    @property
    def max_exposure(self):
        return self._max_exposure

    @max_exposure.setter
    def max_exposure(self, max_exposure):
        self._max_exposure = max_exposure / 100 if max_exposure and max_exposure > 1 else max_exposure

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def efficiency(self):
        return round(self.fppg / self.salary, 2)

