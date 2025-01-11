import pandas as pd
import glob
import os
import json
import xml.etree.ElementTree as ET
import logging

# Log file path
log_file = 'D:\\Downloads\\log_file.txt'

# Output CSV file path
transformed_data_path = 'D:\\Downloads\\transformed_data.csv'

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Define base path where the extracted files are stored (adjust as necessary)
base_path = r'D:\Downloads\source_data'  # Adjust the path to your folder if needed

# Function to extract data from CSV
def extract_csv(file_path):
    logging.info(f"Extracting CSV data from {file_path}")
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Successfully extracted data from {file_path}")
        return datag
    except Exception as e:
        logging.error(f"Error extracting CSV data: {e}")
        return None

# Function to extract data from JSON
def extract_json(file_path):
    logging.info(f"Extracting JSON data from {file_path}")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        df = pd.json_normalize(data)
        logging.info(f"Successfully extracted data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error extracting JSON data: {e}")
        return None

# Function to extract data from XML
def extract_xml(file_path):
    logging.info(f"Extracting XML data from {file_path}")
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        all_data = []
        
        for child in root:
            data = {elem.tag: elem.text for elem in child}
            all_data.append(data)
        
        df = pd.DataFrame(all_data)
        logging.info(f"Successfully extracted data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error extracting XML data: {e}")
        return None

# Master function to extract data based on file type
def extract_data(file_path):
    if file_path.endswith('.csv'):
        return extract_csv(file_path)
    elif file_path.endswith('.json'):
        return extract_json(file_path)
    elif file_path.endswith('.xml'):
        return extract_xml(file_path)
    else:
        logging.error(f"Unsupported file format: {file_path}")
        return None

# Function to transform data (unit conversions)
def transform_data(df):
    logging.info("Starting data transformation...")

    # If 'Height(Inches)' exists, convert to meters
    if 'Height(Inches)' in df.columns:
        df['Height(Meters)'] = df['Height(Inches)'] * 0.0254

    # If 'Weight(Pounds)' exists, convert to kilograms
    if 'Weight(Pounds)' in df.columns:
        df['Weight(Kilograms)'] = df['Weight(Pounds)'] * 0.453592

    logging.info("Data transformation completed.")
    return df

# Function to load transformed data into a CSV file
def load_data(df):
    logging.info(f"Loading data into {transformed_data_path}...")
    try:
        df.to_csv(transformed_data_path, index=True)
        logging.info(f"Data successfully loaded into {transformed_data_path}")
    except Exception as e:
        logging.error(f"Error loading data: {e}")

# Main function to execute the ETL process
def main():
    logging.info("ETL process started.")

    # List all files in the unzipped folder (using base_path to define file location)
    data_files = glob.glob(os.path.join(base_path, '*'))  # Adjust the path if necessary
    
    all_data = []

    # Extract phase
    for file in data_files:
        # Ensure file_path is passed properly to the extract_data function
        extracted_data = extract_data(file)  # Pass the correct file path here
        if extracted_data is not None:
            all_data.append(extracted_data)

    if all_data:
        # Combine all extracted data into a single DataFrame
        df = pd.concat(all_data, ignore_index=True)

        # Transform phase
        transformed_df = transform_data(df)

        # Load phase
        load_data(transformed_df)

    logging.info("\n ETL process completed.")


if __name__ == "__main__":
    main()

