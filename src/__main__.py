import sys
import os
from scraper import WebScraper
from utils import Utils
from pymenu import select_menu

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


try:
    options = ["Update or fetch the indexes.", "Fetch all data cards.", "Exit the app."]
    selected_option = select_menu.create_select_menu(
        options, "Hello! Please select an option."
    )

    tool = WebScraper()
    if selected_option == "Update or fetch the indexes.":
        tool.fetch_indexes()
    elif selected_option == "Fetch all data cards.":
        tool.fetch_all_cards()
    else:
        sys.exit()
except KeyboardInterrupt:
    Utils.clear_console()
    sys.exit()
