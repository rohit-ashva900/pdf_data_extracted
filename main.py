import json
import os
from bulk_processor import bulk_scan_documents


def main():
    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/google_api_key.json'

    input_directory = 'data/input/'
    output_file = 'data/output/extracted_data.json'

    data_model = bulk_scan_documents(input_directory)

    with open(output_file, 'w') as f:
        json.dump(data_model, f, indent=4)

    print(f"Extracted data has been saved to {output_file}")


if __name__ == "__main__":
    main()
