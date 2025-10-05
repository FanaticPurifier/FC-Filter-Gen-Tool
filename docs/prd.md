Product Requirements Document (PRD)
Project: FC Filter Gen Tool
Author: Paul O'Neill
Date: 05 October 2025
Status: Final Draft

1. Introduction & Problem Statement
Millions of players engage with the EA FC Ultimate Team market, where buying and selling players to generate in-game currency is a core activity. Power users ("traders") rely on speed and efficiency to capitalize on market fluctuations. Many use external AI tools that suggest which players to buy and at what price.

The Problem: The process of translating these suggestions into actionable search filters within the EA FC Web App is entirely manual, repetitive, and time-consuming. A user must create a filter for each player, save it, and add it to a larger search group. This process can take hours, is prone to data entry errors, and—most critically—prevents the user from actively trading, leading to significant opportunity cost in a fast-moving market.

The Solution: This project is a desktop utility that automates the creation of the JSON filter file used by the web app's extension. By taking a simple copy-pasted list of players and prices as input, the tool will instantly generate the complex, correctly formatted JSON file, ready for upload.

2. Target Audience
The primary user is an EA FC Ultimate Team "power-user" or "trader."

Behavior: They are highly engaged with the in-game transfer market and actively seek to generate profit. They are comfortable using third-party tools, including browser extensions and AI-driven market analysis websites.

Technical Comfort: They understand the concept of search filters and are technically proficient enough to download/upload a JSON file as part of an existing workflow. They are motivated by efficiency and optimization.

3. Success Metrics
The success of this utility will be measured by its effectiveness and the skills it demonstrates as a portfolio piece.

Time Saved: Reduce the time required to add 20 new player filters from over 30 minutes to under 2 minutes.

Accuracy: Achieve a 100% accuracy rate in the generated JSON, eliminating all manual data entry errors that could cause an import to fail.

Portfolio Goal: Successfully demonstrate core development skills in data parsing, user interaction (CLI), data mapping, and file generation.

4. Functional Requirements & User Stories
As a user, I want to...

...paste a list of players and their recommended buy prices into the application so that I can provide the necessary input quickly.

...run a command to generate a complete JSON filter file that is correctly formatted for the web app extension.

...be prompted to choose the correct player if the application finds multiple matches for a name to ensure the filters are created for the exact players I intend to trade.

...save the generated JSON file directly to my computer so I can immediately upload it to the web app extension.

...see a clear error message if the input is formatted incorrectly or a player cannot be found so I can correct the problem and try again.

5. Scope
In Scope for Version 1.0 (MVP):
An interface for providing copied text as input (CLI recommended).

Parsing logic to extract player names and buy prices from the input.

A data mapping system that uses a local CSV file to look up player IDs and other metadata.

A user prompt to resolve ambiguous player names.

Generation of a complete, valid JSON file.

Functionality to save the generated file to a local directory.

Out of Scope for Version 1.0 (Future Work):
A full graphical user interface (GUI).

A web scraper or API client to fetch live player data automatically.

Direct integration with the browser extension (i.e., automatic upload).

Saving/managing multiple lists or filter sets within the app.