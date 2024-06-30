import pandas as pd

def print_column_details(df):
    """
    Print the column headers of a DataFrame along with the value counts for each column.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to extract and display column details.
    """
    # Prepare to display column headers with value counts
    headers_info = {}

    # Collect column headers and their value counts
    for column in df.columns:
        headers_info[column] = df[column].value_counts().to_frame().T

    # Create a DataFrame to display headers and value counts
    headers_df = pd.DataFrame(index=df.columns)  # This creates an empty DataFrame with column headers as index
    for column, value_counts in headers_info.items():
        headers_df = pd.concat([headers_df, value_counts], ignore_index=False)

    # Print the DataFrame containing the column headers and value counts
    print(headers_df)
if __name__ == "__main__":
    print("This script should not be run directly! Import these functions for use in another file.")
