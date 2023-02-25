TEAM_FULL_NAME_MAP = {
    "Washington Wizards": "WAS",
    "Brooklyn Nets": "BKN",
    "Chicago Bulls": "CHI",
    "Miami Heat": "MIA",
    "Cleveland Cavaliers": "CLE",
    "Philadelphia 76ers": "PHI",
    "New York Knicks": "NYK",
    "Charlotte Hornets": "CHA",
    "Boston Celtics": "BOS",
    "Toronto Raptors": "TOR",
    "Milwaukee Bucks": "MIL",
    "Atlanta Hawks": "ATL",
    "Indiana Pacers": "IND",
    "Detroit Pistons": "DET",
    "Orlando Magic": "ORL",
    "Golden State Warriors": "GSW",
    "Phoenix Suns": "PHX",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Los Angeles Clippers": "LAC",
    "LA Clippers": "LAC",
    "Utah Jazz": "UTA",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "Oklahoma City Thunder": "OKC",
    "Minnesota Timberwolves": "MIN",
    "San Antonio Spurs": "SAS",
    "New Orleans Pelicans": "NOP",
    "Houston Rockets": "HOU",
    "Charlotte Bobcats": "CHA",
    "New Orleans Hornets": "NOP",
    "New Jersey Nets": "BKN",
    "Seattle SuperSonics": "OKC",
    "New Orleans/Oklahoma City Hornets": "NOP",
}

TEAM_SHORT_NAME_MAP = {
    "Nets": "BKN",
    "Celtics": "BOS",
    "Bucks": "MIL",
    "Hawks": "ATL",
    "Hornets": "CHA",
    "Bulls": "CHI",
    "Cavaliers": "CLE",
    "Mavericks": "DAL",
    "Nuggets": "DEN",
    "Pistons": "DET",
    "Warriors": "GSW",
    "Rockets": "HOU",
    "Pacers": "IND",
    "Clippers": "LAC",
    "Lakers": "LAL",
    "Grizzlies": "MEM",
    "Heat": "MIA",
    "Timberwolves": "MIN",
    "Pelicans": "NOP",
    "Knicks": "NYK",
    "Thunder": "OKC",
    "Magic": "ORL",
    "76ers": "PHI",
    "Suns": "PHX",
    "Trail Blazers": "POR",
    "Spurs": "SAS",
    "Kings": "SAC",
    "Raptors": "TOR",
    "Jazz": "UTA",
    "Wizards": "WAS",
}

TEAM_ABBREVIATION_MAP = {
    "BK": "BKN",
    "BRK": "BKN",
    "BKN": "BKN",
    "BOS": "BOS",
    "MIL": "MIL",
    "ATL": "ATL",
    "CHA": "CHA",
    "CHO": "CHA",
    "CHI": "CHI",
    "CLE": "CLE",
    "DAL": "DAL",
    "DEN": "DEN",
    "DET": "DET",
    "GS": "GSW",
    "GSW": "GSW",
    "HOU": "HOU",
    "IND": "IND",
    "LAC": "LAC",
    "LAL": "LAL",
    "MEM": "MEM",
    "MIA": "MIA",
    "MIN": "MIN",
    "NO": "NOP",
    "NOP": "NOP",
    "NY": "NYK",
    "NYK": "NYK",
    "OKC": "OKC",
    "ORL": "ORL",
    "PHI": "PHI",
    "PHO": "PHX",
    "PHX": "PHX",
    "POR": "POR",
    "SA": "SAS",
    "SAS": "SAS",
    "SAC": "SAC",
    "TOR": "TOR",
    "UTA": "UTA",
    "WAS": "WAS",
}


TEAM_MAP = dict(
    TEAM_FULL_NAME_MAP.items()
    | TEAM_SHORT_NAME_MAP.items()
    | TEAM_ABBREVIATION_MAP.items()
)