# Import necessary packages
import pandas as pd
import numpy as np

# Import the necessary files
price = pd.read_csv('data/airbnb_price.csv')
room_type = pd.read_excel('data/airbnb_room_type.xlsx')
last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.

# Convert the 'last_review' column to datetime format
last_review['last_review'] = pd.to_datetime(last_review['last_review'])

# Find the earliest and most recent review dates
earliest_review_date = last_review['last_review'].min()
most_recent_review_date = last_review['last_review'].max()

print(earliest_review_date)
print(most_recent_review_date)

# Count the number of listings that are private rooms
room_type['room_type'] = room_type['room_type'].str.lower()
private_room_count = room_type[room_type['room_type'] == 'private room'].shape[0]


# The variable 'private_room_count' now holds the number of listings that are private rooms.
# The 'room_type' DataFrame is filtered to include only rows where the 'room_type' column is 'private room'.
# The 'shape' attribute of the filtered DataFrame is used to get the number of rows, which corresponds to the count of private room listings.
print(private_room_count)

# Check for NaN values in the 'price' column
nan_count = price['price'].isna().sum()

# Display the count of NaN values
nan_count

# Strip out the " dollars" from the "price" column and convert to numeric type
price['price'] = price['price'].astype(str).str.replace(' dollars', '', regex=True).astype(float)

# Calculate the average listing price and round to two decimal places
average_listing_price = round(price['price'].mean(), 2)

# The variable 'average_listing_price' now holds the rounded average listing price.
average_listing_price


earliest_review_date = last_review['last_review'].min()
most_recent_review_date = last_review['last_review'].max()
nb_private_room_count = room_type[room_type['room_type'] == 'private room'].shape[0]

# Create a DataFrame with the new variables
review_dates = pd.DataFrame({

    'first_reviewed': [earliest_review_date],
    'last_reviewed': [most_recent_review_date],
    'nb_private_rooms': [private_room_count],
    'avg_price': [average_listing_price]
})

# Display the DataFrame
review_dates

