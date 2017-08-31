from .roster import Player, Lineup
from .auxiliary import EnhantasyException, FaultyTeamName, FaultyPositionName, Site, Sport
from .enhantasy import Enhantasy
from .settings import YahooBasketballSettings, YahooFootballSettings, YahooHockeySettings, YahooBaseballSettings, \
    FanDuelBasketballSettings, FanDuelFootballSettings, FanDuelHockeySettings, FanDuelBaseballSettings, \
    DraftKingsBasketballSettings, DraftKingsFootballSettings, DraftKingsHockeySettings, DraftKingsBaseballSettings, \
    FantasyDraftBasketballSettings, FantasyDraftFootballSettings, FantasyDraftHockeySettings


settings_mapping = {
    Site.DRAFTKINGS: {
        Sport.BASKETBALL: DraftKingsBasketballSettings,
        Sport.FOOTBALL: DraftKingsFootballSettings,
        Sport.HOCKEY: DraftKingsHockeySettings,
        Sport.BASEBALL: DraftKingsBaseballSettings,
    },
    Site.FANDUEL: {
        Sport.BASKETBALL: FanDuelBasketballSettings,
        Sport.FOOTBALL: FanDuelFootballSettings,
        Sport.HOCKEY: FanDuelHockeySettings,
        Sport.BASEBALL: FanDuelBaseballSettings,
    },
    Site.YAHOO: {
        Sport.BASKETBALL: YahooBasketballSettings,
        Sport.FOOTBALL: YahooFootballSettings,
        Sport.HOCKEY: YahooHockeySettings,
        Sport.BASEBALL: YahooBaseballSettings,
    },
    Site.FANTASY_DRAFT: {
        Sport.BASKETBALL: FantasyDraftBasketballSettings,
        Sport.FOOTBALL: FantasyDraftFootballSettings,
        Sport.HOCKEY: FantasyDraftHockeySettings,
    },
}


def get_enhantasy(site, sport):
    try:
        return LineupOptimizer(settings_mapping[site][sport])
    except KeyError:
        raise NotImplementedError

