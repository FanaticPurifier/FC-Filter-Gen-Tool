Request for Comments (RFC)
Project: FC Filter Gen Tool
Author: Paul O'Neill
Date: 05 October 2025
Status: Proposed

1. Abstract
This document outlines the proposed technical design for a command-line interface (CLI) tool built in Python. The tool will parse user-provided text containing player trade data, map it against a local data source, and generate a valid JSON file for use in the EA FC Web App extension.

2. Proposed Design & Architecture
Technology Stack
Language: Python 3.9+

CLI Framework: Typer (for its simplicity and robust feature set).

Data Handling: Python's built-in csv module for mapping and json module for templating and output.

Core Components
CLI (app.py): The main entry point. It will use Typer to define commands, arguments (--input, --output), and options.

Input Parser: A module responsible for taking the raw input string (from a text file) and parsing it into a structured list of players and their target buy prices.

Data Mapper: A class or module that loads the players.csv file into memory on startup. It will provide a method to look up player details by a search name, returning all possible matches.

Disambiguation Engine: A simple interactive function that, when the Data Mapper returns multiple player matches, will print a numbered list to the console and ask the user to input the number of the correct player.

JSON Generator: This component will load a template.json file. It will loop through the user's confirmed list of players, and for each player, it will populate the template with the dynamic data (ID, price, name, etc.) and add the resulting object to the final JSON structure.

3. Data Schemas
Mapping Data (players.csv)
A CSV file with the following required columns:

PlayerID	FirstName	LastName	Rating	SearchableName
261733	Sandy	Baltimore	85	Baltimore
225375	Konrad	Laimer	82	Laimer IF

Export to Sheets
Output Data (filters.json)
The application will generate a JSON object matching the following structure. The majority of the file is a static template, with the dynamic fields noted below.

JSON

{
    "filters": {
        "SHARED": { /* Static shared settings object */ },
        "PLAYER_KEY_1": {
            "criteria": {
                /* Most fields are static */
                "maskedDefId": DYNAMIC_PLAYER_ID,
                "maxBuy": DYNAMIC_BUY_PRICE
            },
            "playerData": {
                "id": DYNAMIC_PLAYER_ID,
                "firstName": DYNAMIC_FIRST_NAME,
                "lastName": DYNAMIC_LAST_NAME,
                "rating": DYNAMIC_RATING
            },
            "baseSetting": {
                "buySetting": {
                    "buyPrice": DYNAMIC_BUY_PRICE,
                    /* Other fields are static */
                },
                /* Other settings are static */
            }
        },
        "PLAYER_KEY_2": { /* ... more player objects */ }
    }
}
4. Error Handling
The application must handle errors gracefully by printing a clear message to the console and exiting.

Parsing Error: If the input text file's format is unrecognizable.

Player Not Found: If a player name from the input cannot be found in players.csv.

File I/O Error: If the players.csv mapping file is missing or the output file cannot be written.

5. Future Considerations
For V2, the reliance on a local CSV file should be replaced. The ideal solution is to find and use a public API from a service like Futbin. If no API is available, a web scraper (using libraries like BeautifulSoup or Scrapy) will be developed. The application architecture should be modular enough to allow the Data Mapper's source to be swapped from a local CSV reader to an API client or scraper without affecting other components.