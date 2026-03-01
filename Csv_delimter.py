import csv
import pandas as pd 

#get user input csv file
input_csv_file = input("Enter the name of the input CSV file (including .csv extension): ")

#read input csv file and convert to pandas dataframe
data = pd.read_csv(input_csv_file)

#read csv to get original column names 
original_column_names = data.columns.tolist()

#store orriginal column names in a list
original_column_names_list = []
for column in original_column_names:
    original_column_names_list.append(column)

#enumerate original column names for user reference
enumerate_column_names = list(enumerate(original_column_names_list, start=1))
print("Enumerated column names: ", enumerate_column_names)

#allow user to select column names from the enumerated list and input new column names for the output csv file or remove if they skip it by pressing enter
def get_user_column_names():
    mappings = []
    for i, orig_col in enumerate(original_column_names_list, start=1):
        user_column_name = input(f"Enter the name of the column {i} (or press Enter to skip): ").strip()
        if user_column_name:
            mappings.append((orig_col, user_column_name))
        else:
            if orig_col in data.columns:
                data.pop(orig_col)
    return mappings

#create new dataframe with user defined column names 
def create_new_dataframe(data, mappings):
    new_dataframe = pd.DataFrame()
    for orig_col, new_name in mappings:
        if orig_col in data.columns:
            new_dataframe[new_name] = data[orig_col]
        else:
            print(f"Warning: original column '{orig_col}' not found; skipping.")
    return new_dataframe

#main function to execute the program 
def main():
    user_mappings = get_user_column_names()
    new_dataframe = create_new_dataframe(data, user_mappings)
    output_csv_file = input("Enter the name of the output CSV file (including .csv extension): ")
    new_dataframe.to_csv(output_csv_file, index=False)
    print(f"New CSV file '{output_csv_file}' has been created with the selected columns.")


if __name__ == "__main__":
    main()


