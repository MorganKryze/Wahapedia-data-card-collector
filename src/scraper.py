from selenium.webdriver import FirefoxOptions as Options, Firefox as Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
import time

from utils import Utils


class WebScraper:
    def __init__(self):
        self.output_dir = "./out/factions/"
        self.source_dir = "./out/source/"

        self.base_url = "https://wahapedia.ru/wh40k10ed/"
        self.factions_url = self.base_url + "factions/"
        self.home_url = "https://wahapedia.ru/wh40k10ed/the-rules/quick-start-guide/"

        self.check_for_cookies = True

        self.driver = None
        self.factions_names = []
        self.factions_dict = {}

    @Utils.loading(
        "Ensuring output directories exist...",
        "Output directories exist.",
        "Failed to ensure output directories exist.",
    )
    def ensure_dirs_exist(self):
        try:
            os.makedirs(self.output_dir, exist_ok=True)
            os.makedirs(self.source_dir, exist_ok=True)
            return 0
        except Exception:
            return 1

    @Utils.loading(
        "Installing uBlock Origin...",
        "uBlock Origin installed.",
        "Failed to install uBlock Origin.",
    )
    def install_ublock(self):
        try:
            ublock_url = "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/addon-1318898-latest.xpi"
            ublock_path = "./docs/assets/extensions/ublock_origin.xpi"

            if not os.path.exists(ublock_path):
                response = requests.get(ublock_url)
                with open(ublock_path, "wb") as file:
                    file.write(response.content)

            self.driver.install_addon(ublock_path)
            return 0
        except Exception:
            return 1

    def get_names_from_html(self, html):
        links = html.find_elements(By.TAG_NAME, "a")
        hrefs = [link.get_attribute("href") for link in links]
        names = [href.split("/")[-1] for href in hrefs]

        # Remove datasheets.html as it is not a valid name
        names = [name for name in names if name != "datasheets.html"]
        return names

    def init_session(self, width=2560, height=1440, headless=True):
        driver_options = Options()
        driver_options.add_argument("--width=" + str(width))
        driver_options.add_argument("--height=" + str(height))
        if headless:
            driver_options.add_argument("--headless")

        self.driver = Browser(options=driver_options)
        self.ensure_dirs_exist()
        self.install_ublock()
        self.remove_cookies()

    @Utils.loading(
        "Closing session...",
        "Session closed.",
        "Failed to close session.",
    )
    def close_session(self):
        try:
            self.driver.quit()
            return 0
        except Exception:
            return 1

    @Utils.loading(
        "Removing cookies...",
        "Cookies removed.",
        "Failed to remove cookies.",
    )
    def remove_cookies(self):
        if not self.check_for_cookies:
            return 0
        self.driver.get(self.home_url)
        try:
            cookies_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ez-manage-settings"]'))
            )
            cookies_button.click()
        except Exception:
            return 1

        try:
            save_exit_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ez-save-settings"]'))
            )
            save_exit_button.click()
        except Exception:
            return 1

        self.check_for_cookies = False
        return 0

    @Utils.loading(
        "Fetching factions names...",
        "Factions names fetched.",
        "Failed to fetch factions names.",
    )
    def fetch_factions_names(self):
        try:
            self.driver.get(self.home_url)

            menu = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[2]/div",
                    )
                )
            )

            self.factions_names = self.get_names_from_html(menu)
            return 0
        except Exception:
            return 1

    @Utils.loading(
        "Fetching units names from faction name...",
        "Units names fetched.",
        "Failed to fetch units names from their faction names.",
    )
    def fetch_units_names_from_faction(self, faction_name):
        try:
            self.driver.get(self.factions_url + faction_name)

            button = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="btnArmyList"]'))
            )
            actions = ActionChains(self.driver)

            actions.move_to_element(button).perform()

            time.sleep(1)
            tooltip = self.driver.find_elements(
                By.XPATH, '//*[@id="tooltip_contentArmyList"]'
            )

            self.factions_dict[faction_name] = self.get_names_from_html(tooltip[1])
            return 0
        except Exception:
            return 1

    def fetch_card_from_unit(self, faction, unit):
        # Gets the page
        self.driver.get(self.factions_url + faction + "/" + unit)

        # Remove the army list button
        self.driver.execute_script(
            """
            document.querySelector("#btnArmyList").remove();
            """
        )

        # Ensure the output directory exists
        os.makedirs(self.output_dir + faction, exist_ok=True)

        # Isolate the card and take a screenshot
        data_card = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[4]'))
        )
        data_card.screenshot(self.output_dir + faction + "/" + unit + ".png")

    def fetch_indexes(self):
        try:
            self.init_session()

            self.fetch_factions_names()
            self.factions_dict = Utils.init_dictionary_with_keys(self.factions_names)

            for faction_name in self.factions_names:
                self.fetch_units_names_from_faction(faction_name)

            Utils.save_dict_to_json(self.factions_dict, self.source_dir + "source")

            self.close_session()
            return 0
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            self.close_session()
            return 1
        except Exception as e:
            self.close_session()
            print(e)
            return 1

    def fetch_all_cards(self):
        cards_to_fetch = Utils.load_dictionary_if_exists(self.source_dir)
        if cards_to_fetch is None:
            return 1

        try:
            self.init_session()

            for faction, units in cards_to_fetch.items():
                for unit in units:
                    self.fetch_card_from_unit(faction, unit)
                    cards_to_fetch[faction].remove(unit)

            self.close_session()
            return 0
        except KeyboardInterrupt:
            print(
                "\nProcess interrupted by user. The dictionary will be saved to temp.json."
            )
            self.close_session()
            Utils.save_dict_to_json(cards_to_fetch, self.source_dir + "temp")
            return 1
        except Exception as e:
            print("An error occurred. The dictionary will be saved to temp.json.")
            print(e)
            self.close_session()
            Utils.save_dict_to_json(cards_to_fetch, self.source_dir + "temp")
            return 1
