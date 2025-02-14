import pandas as pd
import matplotlib.pyplot as plt
import os

from pyparsing import html_comment

# Define the correct file path
file_path = r"C:\Users\kowsa\python\exam.csv"  # Change this to your actual file location

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
else:
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Check if the 'RESULT' column exists
    if 'RESULT' in df.columns:
        # Count pass and fail
        pass_fail_counts = df['RESULT'].value_counts()

        # Plot the pie chart
        plt.figure(figsize=(7,7))
        plt.pie(pass_fail_counts, labels=pass_fail_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
        
        # Add title
        plt.title("Pass vs Fail Distribution")

        # Show the plot
        plt.show()

    
