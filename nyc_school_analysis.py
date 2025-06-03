import pandas as pd

# Load the dataset
schools = pd.read_csv("schools.csv")

# Preview the data (optional)
print(schools.head())

# Set cutoff threshold for top math performers (80% of max score 800 = 640)
math_cutoff = 0.8 * 800

# Filter schools with average math scores >= 640
best_math_schools = schools[schools["average_math"] >= math_cutoff][["school_name", "average_math"]]
best_math_schools = best_math_schools.sort_values(by="average_math", ascending=False)

# Display top 10 schools based on math scores
print("Top 10 Schools by Math Scores:")
print(best_math_schools.head(10))

# Calculate total SAT score for each school
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Get top 10 schools by total SAT score
top_10_schools = schools.sort_values(by="total_SAT", ascending=False).head(10)[["school_name", "total_SAT"]]
print("\nTop 10 Schools by Total SAT Score:")
print(top_10_schools)

# Reload data to avoid side effects (optional, if doing multiple stages)
schools = pd.read_csv("schools.csv")

# Calculate total SAT again
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Group by borough and calculate school count, mean, and std deviation
borough_stats = schools.groupby("borough").agg(
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", "mean"),
    std_SAT=("total_SAT", "std")
).reset_index()

# Identify borough with highest variation in SAT scores
largest_std_dev = borough_stats.loc[borough_stats["std_SAT"].idxmax()]

# Format and round the result
largest_std_dev = pd.DataFrame([{
    "borough": largest_std_dev["borough"],
    "num_schools": int(largest_std_dev["num_schools"]),
    "average_SAT": round(largest_std_dev["average_SAT"], 2),
    "std_SAT": round(largest_std_dev["std_SAT"], 2)
}])

# Display the borough with the largest SAT score variation
print("\nBorough with Largest SAT Score Variation:")
print(largest_std_dev)
