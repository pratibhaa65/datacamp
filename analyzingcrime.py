# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head

# Ensure 'TIME OCC' is treated as a string
crimes['TIME OCC'] = crimes['TIME OCC'].astype(str)

# Extract the hour from 'TIME OCC' (assuming the format is "HH:MM")
crimes['Hour'] = crimes['TIME OCC'].str[:2].astype(int)

# Plot the count of crimes by hour
sns.countplot(x='Hour', data=crimes)

# Find the peak crime hour (the hour with the highest number of crimes)
peak_crime_hour = crimes['Hour'].value_counts().idxmax()

# Print the peak crime hour
print(f"The peak crime hour is: {peak_crime_hour}:00")

# Convert 'TIME OCC' to numeric, forcing errors to NaN
crimes['TIME OCC'] = pd.to_numeric(crimes['TIME OCC'], errors='coerce')

# Extract the hour from 'TIME OCC' (e.g., 2300 -> 23, 0315 -> 3)
crimes['Hour'] = crimes['TIME OCC'].astype(str).str[:2].astype(int)

# Filter for night crimes (between 10 PM and 4 AM)
night_crimes = crimes[(crimes['Hour'] >= 22) | (crimes['Hour'] <= 4)]

# Group by 'AREA NAME' and count the number of occurrences
location_counts = night_crimes['AREA NAME'].value_counts()

# Get the location with the highest count
peak_night_crime_location = location_counts.idxmax()

print(f"The location with the most night crimes is: {peak_night_crime_location}")

age_bins = [0, 17, 25, 34, 44, 54, 64, float("inf")]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
crimes['Age_Group'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels, right=True)
victim_ages = crimes['Age_Group'].value_counts().reindex(age_labels, fill_value=0)
print(victim_ages)