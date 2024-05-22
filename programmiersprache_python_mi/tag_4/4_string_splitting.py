"""
Einen String anhand eines Trenners aufsplitten

"""

user_input = "23,89,12.5662" # x, y, z
user_input_list = user_input.split(",") # Trenner ist Komma
print(user_input_list)

x = float(user_input_list[0])
y = float(user_input_list[1])
z = float(user_input_list[2])

satz = "the quick brown fox"
wörter = satz.split() # Default Trenner ist das Leerzeichen
print(wörter)