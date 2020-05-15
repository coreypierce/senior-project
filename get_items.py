from get_file import get_file
import json
def get_item_list():
    item_dictionary = get_file("http://ddragon.leagueoflegends.com/cdn/10.10.3208608/data/en_US/item.json")

    item_dictionary_data = item_dictionary["data"]

    for key in item_dictionary_data:
        print(item_dictionary_data[key]["name"])