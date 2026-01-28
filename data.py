import pandas as pd

FILE_NAME = "players.csv"

def load_players ():

    players_table = pd.read_csv(FILE_NAME, sep=";")

# Remove extra spaces

    players_table.columns = [col.strip() for col in players_table.columns]

    players_table["Name"] = players_table["Name"].str.strip()

    return players_table

print (load_players())


