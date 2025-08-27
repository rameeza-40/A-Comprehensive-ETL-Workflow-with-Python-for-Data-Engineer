# **A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineer**


### *Project Overview*  
This project demonstrates a complete Extract, Transform, Load (ETL) workflow using Python. The aim is to process data from multiple formats (CSV, JSON, XML), transform it into a standard format with unit conversions, and store the results in a unified CSV file. The project is designed to showcase the capabilities of data engineers in managing heterogeneous datasets and preparing them for further analysis or storage.

##  <ins>*Key Features:*</ins> 
  
  ### Data Extraction:
  * *Supports multiple file formats: CSV, JSON, XML.*
  * *Modular functions for each file type to handle extraction.*

  ### Data Transformation:
  
  #### Converts measurements:
  * *Heights from inches to meters.*
  * *Weights from pounds to kilograms.*
  * *Combines data from different formats into a single DataFrame.*
### Data Loading:
* *Saves the transformed data into a structured CSV file for further use.*
### Logging and Monitoring::
* *Comprehensive logging for each phase (Extraction, Transformation, Loading).*
* *Logs are stored in a text file for traceability and debugging.*
### Reusable and Scalable:
* *Modularized functions for easy integration and reuse.*
* *Scalable to include additional file formats or transformations.*
### Cross-format Compatibility:
* *Handles data inconsistencies across formats with standardized processing.*

## Steps to Execute the Project
### Step 1: Set Up Environment
* *Install Python (if not already installed).*
* *Install required libraries: pandas, glob, xml.etree.ElementTree.*
* *Set up paths for:*
* *log_file.txt for logging.*
* *transformed_data.csv for saving results.*
<br/>

### Step 2: Data Extraction
#### Write extraction functions for each data format:
* *CSV: Use pandas.read_csv().*
* *JSON: Use json.load() and normalize with pandas.json_normalize().*
* *XML: Parse using xml.etree.ElementTree and construct a DataFrame.*
* *Combine extracted data into a single DataFrame using pandas.concat().*
<br/>

### Step 3: Data Transformation
#### Transform data for standardization:
* *Convert heights (inches → meters).*
* *Convert weights (pounds → kilograms).*
* *Validate and clean data as needed.*
<br/>

### Step 4: Data Loading
* *Save the transformed data into a CSV file using pandas.DataFrame.to_csv().*
<br/>

# <ins> *Technologies Used*<ins>
##### * *Programming Language: Python.*
##### * *Data Formats Supported: CSV, JSON, XML*
<br/>


