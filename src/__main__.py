import sys
import os
from scraper import WebScraper
from utils import Utils
from pymenu import select_menu

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


try:
    options = ["Update or fetch the indexes.", "Fetch all data cards.","Fetch data cards from a faction", "Exit the app."]
    selected_option = select_menu.create_select_menu(
        options, "Hello! Please select an option and press Enter:"
    )

    tool = WebScraper()
    if selected_option == "Update or fetch the indexes.":
        tool.fetch_indexes()
    elif selected_option == "Fetch all data cards.":
        tool.fetch_all_cards()
    elif selected_option == "Fetch data cards from a faction":
        factions = Utils.load_dictionary_if_exists(tool.source_dir).keys()
        if factions is None:
            print("No dictionary found. Please fetch the indexes first.")
            sys.exit()
        factions_choices = list(factions)
        factions_choices.append("Exit the app.")
        selected_faction = select_menu.create_select_menu(
            factions_choices, "Please select a faction and press Enter:"
        )
        if selected_faction != "Exit the app.":
            tool.fetch_all_cards_from_faction(selected_faction)
        else:
            sys.exit()
    else:
        sys.exit()
except KeyboardInterrupt:
    Utils.clear_console()
    sys.exit()
