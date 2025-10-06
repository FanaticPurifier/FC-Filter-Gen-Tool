import sys
from fc_filter_gen.input_parser import parse_and_map_trades
from fc_filter_gen.data_mapper import DataMapper
from fc_filter_gen.json_generator import generate_output_json
import os

def main():
    print("Paste your player trade list below. Enter a blank line to finish:")
    input_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            input_lines.append(line)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nInput cancelled.")
            return

    input_text = "\n".join(input_lines)

    # Load player ID mapping
    try:
        data_mapper = DataMapper("fc_filter_gen/player_id_mapping.csv")
    except Exception as e:
        print(f"Error loading player_id_mapping.csv: {e}")
        return

    # Parse and map trades
    results = parse_and_map_trades(input_text, data_mapper)

    # Prompt for template and output file paths
    default_template = "fc_filter_gen/reference_docs/sample_filters/filters (3).json"
    default_output = "fc_filter_gen/generated_filters.json"
    template_path = input(f"Template JSON path [{default_template}]: ").strip() or default_template
    output_path = input(f"Output JSON path [{default_output}]: ").strip() or default_output

    # Generate output JSON
    try:
        generate_output_json(results, template_path, output_path)
        print(f"\nSuccess! Output written to {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"Error generating output JSON: {e}")

if __name__ == "__main__":
    main()
