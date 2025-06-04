# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Load the dataset
file_path = "data/nobel.csv" 
df = pd.read_csv(file_path)

# Check the columns of the dataframe to ensure 'Year' exists
print(df.columns)
df.head(20)

# Create a Decade column
df["Decade"] = (df["year"] // 10) * 10

# 1. Most commonly awarded gender and birth country
top_gender = df["sex"].mode()[0]
top_country = df["birth_country"].mode()[0]

print(top_gender)
print(top_country)

# 2. Decade with the highest ratio of US-born winners to total winners

# Ensure the 'Decade' column exists or create it if it doesn't
if 'Decade' not in df.columns:
    df['Decade'] = (df['year'] // 10) * 10

total_winners_per_decade = df.groupby("Decade")["full_name"].count()
print(total_winners_per_decade)

us_winners_per_decade = df[df["birth_country"] == "United States of America"].groupby("Decade")["full_name"].count()

ratio_per_decade = (us_winners_per_decade / total_winners_per_decade).fillna(0)
max_decade_usa = ratio_per_decade.idxmax()

print(max_decade_usa)


# 3. Decade & category with the highest proportion of female laureates

# Ensure the 'Decade' column exists or create it if it doesn't
if 'Decade' not in df.columns:
    df['Decade'] = (df['year'] // 10) * 10
    
total_per_category_decade = df.groupby(["Decade", "category"])["full_name"].count()
# print(total_per_category_decade)

female_per_category_decade = df[df["sex"] == "Female"].groupby(["Decade", "category"])["full_name"].count()
# print(female_per_category_decade)

female_ratio = (female_per_category_decade / total_per_category_decade).fillna(0)
# print(female_ratio)

max_female_entry = female_ratio.idxmax()
max_female_dict = {max_female_entry[0]: max_female_entry[1]}


print(max_female_dict)

# 4. First woman to receive a Nobel Prize
first_woman = df[df["sex"] == "Female"].sort_values("year").iloc[0]
first_woman_name = first_woman["full_name"]
first_woman_category = first_woman["category"]
print(first_woman_name , first_woman_category )


# 5. Individuals/organizations that have won multiple Nobel Prizes
repeat_winners = df["full_name"].value_counts()
repeat_list = repeat_winners[repeat_winners > 1].index.tolist()
print(repeat_winners)
print(repeat_list)


# Display results
print(f"Most common gender: {top_gender}")
print(f"Most common birth country: {top_country}")
print(f"Decade with highest US-born winners ratio: {max_decade_usa}")
print(f"Decade & Category with highest female proportion: {max_female_dict}")
print(f"First female laureate: {first_woman_name} ({first_woman_category})")
print(f"Multiple-time winners: {repeat_list}")