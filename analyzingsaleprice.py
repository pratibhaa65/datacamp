import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

df = pd.read_csv('/home/prativa/Documents/projects/dataset1.csv')

# Remove the first column 
df = df.iloc[: , 1:]
df.head()

# Rename the columns to more meaningful names
headers = ["symboling", "normalized-losses", "make", 
           "fuel-type", "aspiration","num-of-doors",
           "body-style","drive-wheels", "engine-location",
           "wheel-base","length", "width","height", "curb-weight",
           "engine-type","num-of-cylinders", "engine-size", 
           "fuel-system","bore","stroke", "compression-ratio",
           "horsepower", "peak-rpm","city-mpg","price"]
headers = headers[:25]  # Keep first 25 headers
df.columns=headers
df.head()

# Check for missing values in the dataset
# This will return a boolean Series indicating if any value is missing in each column
data = df
data.isna().any()
data.isnull().any()

#  Converting MPG to L/100km
data['city-mpg'] = 235 / df['city-mpg']
data.rename(columns = {'city-mpg': "city-L / 100km"}, inplace = True)
print(data.columns)
data.dtypes

# Convert 'price' column to numeric, handling non-numeric values
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data.price.unique()
data = data[data.price != '?']
data['price'] = data['price'].astype(int)
data.dtypes


# normalizing the data
data['length'] = data['length']/data['length'].max()
data['width'] = data['width']/data['width'].max()
data['height'] = data['height']/data['height'].max()


# binning- grouping values
bins = np.linspace(min(data['price']), max(data['price']), 4) 
group_names = ['Low', 'Medium', 'High']
data['price-binned'] = pd.cut(data['price'], bins, 
                              labels = group_names, 
                              include_lowest = True)

print(data['price-binned'])
plt.hist(data['price-binned'])
plt.show()

# Convert 'fuel-type' to dummy variables
data['fuel-type'] = data['fuel-type'].astype('category')
pd.get_dummies(data['fuel-type']).head()
data.describe()


# boxplot of 'price' column
plt.boxplot(data['price'])
sns.boxplot(x ='drive-wheels', y ='price', data = data)

# Scatterplot of 'engine-size' vs 'price'
plt.scatter(data['engine-size'], data['price'])
plt.title('Scatterplot of Enginesize vs Price')
plt.xlabel('Engine size')
plt.ylabel('Price')
plt.grid()
plt.show()

# Group by 'drive-wheels' and 'body-style' to analyze the mean price
test = data[['drive-wheels', 'body-style', 'price']]
data_grp = test.groupby(['drive-wheels', 'body-style'], 
                         as_index = False).mean()

data_grp


# Pivot the grouped data to create a matrix for visualization
data_pivot = data_grp.pivot(index = 'drive-wheels',
                            columns = 'body-style')
data_pivot

plt.pcolor(data_pivot, cmap ='RdBu')
plt.colorbar()
plt.show()

