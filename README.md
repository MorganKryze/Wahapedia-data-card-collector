![screenshot](./docs/assets/img/screenshot.png)

## Overview

> A web scrapping tool that allows you to collect data cards from the Wahapedia website.

Wahapedia data cards collector is a web scrapping tool that allows you to collect data cards from the [Wahapedia website](https://wahapedia.ru/). The tool is written in Python and uses the [Selenium](https://www.selenium.dev/) library to automate the process of collecting data cards.

## Getting Started

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Documentation](#documentation)
  - [Setting up](#setting-up)
    - [Prerequisites](#prerequisites)
    - [Install](#install)
    - [Build \& Run](#build--run)
    - [Usage](#usage)
  - [Future improvements](#future-improvements)
  - [Contributing](#contributing)
  - [License](#license)

### Documentation

Under the `src` directory, you will find the following files:

- `scraper.py`: Contains the `WebScraper` class that allows you to fetch the data cards from the Wahapedia website.
- `utils.py`: Contains the `Utils` class that adds functionalities functions to the web scraper.
- `__main__.py`: Contains the main function that allows you to run the tool using the command `python src`.

The code has been typed and documented inlined, so you can check the code for more information. You can also [open an issue](https://github.com/MorganKryze/Wahapedia-data-cards-collector/issues) regarding any inquiries you may have.

Once you setup the tool locally, an `/out` directory will be created. This directory will contain the following folders:

- `factions`: Contains the data cards fetched from the Wahapedia website.
- `source`: Contains the `index.json` file that lists all the factions and cards to fetch (and the `temp.json` when a job has not been completed).

### Setting up

#### Prerequisites

- Python 3.9 or higher
- Git
- Firefox

> [!NOTE]
> The tool uses Firefox as the default browser to run the web scrapping process. You can change the browser by modifying the `src/scraper.py` file:
>
> ```python
> # src/scraper.py
> 1 from selenium.webdriver import FirefoxOptions as Options, Firefox as Browser
> 2 ...
> ```

#### Install

Clone the repository:

```bash
git clone https://github.com/MorganKryze/Wahapedia-data-cards-collector.git
```

You may move to the project directory if you intend to run the tool:

```bash
cd Wahapedia-data-cards-collector
```

#### Build & Run

First we need to create a virtual environment:

```bash
python -m venv wahapedia
```

Then we need to activate the virtual environment:

```bash
source wahapedia/bin/activate
```

Then we need to install the dependencies:

```bash
pip install -r requirements.txt
```

Then we need to run the tool:

```bash
python src
```

#### Usage

The tool is only designed to:

- Create or update an index file (index.json) that lists all the factions and cards to fetch.
- Fetch the data cards from the Wahapedia website for all factions.
- Fetch the data cards from the Wahapedia website for a specific faction.

> [!NOTE]
> The tool will create a `temp.json` file in the `/out/source` directory if a job has not been completed that will be used to resume the job. You can delete this file if you want to start a new job.

![demo](./docs/assets/img/demo.gif)

### Future improvements

- Move to an api-based solution.

### Contributing

If you want to contribute to the project, you can follow the steps described in the [CONTRIBUTING](./.github/CONTRIBUTING) file.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

> [!WARNING]
> This project does not aim to appropriate the content of the [Wahapedia website](https://wahapedia.ru/), but to provide a tool to collect public data cards for personal use only. The owner of this repository will not be held responsible for the use of the data collected by this tool.
