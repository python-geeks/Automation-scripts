import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from a CSV or Excel file
def load_data(file_path):
    """Load data from a CSV or Excel file."""
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please use .csv or .xlsx")
    return data

# Function to clean data
def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values with the mean for numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    
    # Drop rows with missing values in non-numerical columns
    df = df.dropna()
    
    return df

# Function to visualize data
def visualize_data(df, column_name):
    """Generate bar and pie charts for a specified column in the DataFrame."""
    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Generate a bar chart
    df[column_name].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Bar Chart of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Generate a pie chart
    df[column_name].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title(f'Pie Chart of {column_name}')
    plt.ylabel('')  # Hide the y-label
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Specify the file path (change this to your file location)
    file_path = 'data.csv'  # Replace with your CSV or Excel file path
    
    try:
        # Load the data
        data = load_data(file_path)
        print("Data Loaded Successfully!")
        
        # Display the first few rows of the data
        print("\nFirst few rows of the data:")
        print(data.head())
        
        # Clean the data
        cleaned_data = clean_data(data)
        print("\nData Cleaned Successfully!")
        
        # Display the cleaned data
        print("\nFirst few rows of the cleaned data:")
        print(cleaned_data.head())
        
        # Visualize a specified column
        column_name = input("\nEnter the column name you want to visualize: ")
        visualize_data(cleaned_data, column_name)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()