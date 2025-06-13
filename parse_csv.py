import csv

def parse_underwriting_data():
    """Parse the CSV file and print address, county, and census block group for each row."""
    filename = '_TAM_Midas_Base_Data_Set.csv'
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                address = row.get('full_address', 'N/A')
                county = row.get('county', 'N/A')
                census_block = row.get('attom_census_block_group', 'N/A')
                
                print(f"Address: {address}")
                print(f"County: {county}")
                print(f"Census Block Group: {census_block}")
                print("-" * 50)
                
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    parse_underwriting_data()