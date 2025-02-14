from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import os
from js import document

# Adding output to the container in the HTML
document.getElementById("output").innerHTML = "<p>Welcome to the Student Performance Prediction System!</p>"

# Load the CSV file
file_path = "exam.csv"

def analyze_gender_distribution_pie_chart(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    df = pd.read_csv(file_path)

    # Check if required columns exist
    if 'DEPARTMENT' not in df.columns or 'GENDER' not in df.columns:
        print("Error: 'DEPARTMENT' or 'GENDER' column not found in the CSV file.")
        return

    # Group and count gender by department
    gender_counts = df.groupby('DEPARTMENT')['GENDER'].value_counts()

    # Plot pie charts for each department
    departments = gender_counts.index.levels[0]
    for department in departments:
        department_data = gender_counts[department]
        department_data.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), title=f"Gender Distribution in {department}")
        plt.ylabel("")  # Hide the y-axis label for a cleaner chart
       
        # Convert plot to HTML using mpld3
        html_charts += mpld3.fig_to_html(Figure)

        # Close the plot to free memory
        plt.close(plt.figure)

    # Save all charts to a single HTML file
    with open("analysis.html", "w") as f:
        f.write(html_charts)

    print("HTML file 'analysis.html' has been created.")