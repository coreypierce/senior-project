from get_file import get_file
import json
def get_champ_list():
    champ_dictionary = get_file("http://ddragon.leagueoflegends.com/cdn/10.10.3208608/data/en_US/champion.json")

    champ_dictionary_data = champ_dictionary["data"]

    for key in champ_dictionary_data:
        print(champ_dictionary_data[key]["name"])