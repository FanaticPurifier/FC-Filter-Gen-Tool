import csv

class DataMapper:
    def __init__(self, csv_filepath="player_id_mapping.csv"):
        self.players = []
        try:
            with open(csv_filepath, mode='r', encoding='utf-8') as f:
                # DictReader is ideal as it uses the header row for dictionary keys.
                reader = csv.DictReader(f)
                for row in reader:
                    self.players.append(row)
            if self.players:
                print(f"Successfully loaded {len(self.players)} players from {csv_filepath}")
            else:
                print(f"Warning: No players loaded from {csv_filepath}. Is the file empty or in the wrong format?")

        except FileNotFoundError:
            print(f"Error: The file '{csv_filepath}' was not found in this directory.")
            raise
        except Exception as e:
            print(f"An error occurred while reading the CSV: {e}")
            raise
    def search_by_name(self, search_term):
        """
        Searches for players whose 'name' contains the search_term.
        This is case-insensitive.
        Returns a list of matching player dictionaries.
        
        *** NOTE: This assumes your CSV has a column named 'Name'. ***
        *** If it's different (e.g., 'player_name'), change p['Name'] below. ***
        """
        search_term = search_term.lower()
        matches = [
            p for p in self.players
            if 'Name' in p and search_term in p['Name'].lower()
        ]
        return matches
# --- Test Block ---
# This code runs when you execute `python data_mapper.py`
if __name__ == "__main__":
    mapper = DataMapper()

    if mapper.players:
        # Test case 1
        print("\n--- Searching for 'laimer' ---")
        results_laimer = mapper.search_by_name('laimer')
        if results_laimer:
            for player in results_laimer:
                # NOTE: Assumes your CSV has 'name' and 'id' columns.
                print(f"Found: {player['Name']} (ID: {player['ID']})")
        else:
            print("No players found for 'laimer'.")

        # Test case 2
        print("\n--- Searching for 'baltimore' ---")
        results_baltimore = mapper.search_by_name('baltimore')
        if results_baltimore:
            for player in results_baltimore:
                print(f"Found: {player['Name']} (ID: {player['ID']})")
        else:
            print("No players found for 'baltimore'.")