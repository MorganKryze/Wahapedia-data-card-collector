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

...

### Setting up

#### Prerequisites

- Python 3.9 or higher
- Git

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
- Fetch the data cards from the Wahapedia website.

![demo](./docs/assets/img/demo.gif)

### Future improvements

- Move to an api-based solution.

### Contributing

If you want to contribute to the project, you can follow the steps described in the [CONTRIBUTING](./.github/CONTRIBUTING) file.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

> [!WARNING]
> This project does not aim to appropriate the content of the [Wahapedia website](https://wahapedia.ru/), but to provide a tool to collect public data cards for personal use only. The owner of this repository is not responsible for the use of the data collected by this tool.
