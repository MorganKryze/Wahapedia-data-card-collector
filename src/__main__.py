import sys
import os
from scraper import WebScraper
from utils import Utils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

Utils.clear_console()

tool = WebScraper()
# tool.fetch_indexes()
# tool.fetch_all_cards()
