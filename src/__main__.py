import sys
import os
from scraping import Scraping
from utils import Utils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

Utils.clear_console()

tool = Scraping()
tool.create_index()
