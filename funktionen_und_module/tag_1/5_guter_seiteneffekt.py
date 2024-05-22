"""
Guter Seiteneffekt: Game Zustände

"""


game_stat = {
    "bilbo": {
        "life": 89,
        "power": 12,
        "weapons": {"knife", "light"}
    },
     "gollum": {
        "life": 59,
        "power": 32,
        "weapons": set()
     }
}
def add_player_life_points(player, points):
    game_stat[player]["life"] += points


add_player_life_points("gollum", 5)