from difflib import SequenceMatcher

def list_intersection(first_list, second_list):
    return set(first_list).intersection(set(second_list))

def ratio(search_string, possible_match):
    search_string = search_string.lower()
    possible_match = possible_match.lower()
    if len(search_string) >= len(possible_match):
        parts = [possible_match]
    else:
        shorter_length = len(search_string)
        num_of_parts = len(possible_match) - shorter_length
        parts = [possible_match[i:i + shorter_length] for i in range(num_of_parts + 1)]
    return max([SequenceMatcher(None, search_string, part).ratio() for part in parts])

class Site:
    DRAFTKINGS = 'DRAFTKINGS'
    FANDUEL = 'FANDUEL'
    YAHOO = 'YAHOO'
    FANTASY_DRAFT = 'FANTASY_DRAFT'

class Sport:
    BASKETBALL = 'BASKETBALL'
    FOOTBALL = 'FOOTBALL'
    HOCKEY = 'HOCKEY'
    BASEBALL = 'BASEBALL'

class EnhantasyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class FaultyTeamName(EnhantasyException):
    pass

class FaultyPositionName(EnhantasyException):
    pass