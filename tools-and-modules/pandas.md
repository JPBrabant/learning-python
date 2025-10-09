# Naming convention

```python
import pandas as pd
df = pd.read_csv()
```

# Data inspection

```python
df.head()     # Shows first rows of data frame
df.info()     # Displays dataframe info and data types
df.describe() # Shows summary statistics of numeric columns
```

# Missing data handling

```python
df.isnull().sum() # Counts null values per column
df.dropna()       # Remove rows with missing values
df.fillna(value)  # Replace missing values with specified value
```

# Data cleaning & transformation

```python
df.drop_duplicates()              # Remove duplicate rows from dataframe
df.rename(columns={"old": "new"}) # Rename columns using dictionary mapping
df.astype({"col": "type"})        # Convert column data types
df.replace(["old"], ["new"])      # Replace values in dataframe
df.reset_index()                  # Reset index to default numeric sequence
df.drop(["col"], axis=1)          # Removes specified columns
```

# Data selection & filtering

```python
df.loc["label", "col"] # Selects data by labels/conditions
df.iloc[x, y]          # Access data using integer positions
df[df["col"] > value]  # Filters rows based on condition
```

# Data aggregation & analysis

```python
df.groupby("col").agg(["mean"])        # Groups and applies aggregation function
df.sort_values("col", ascending=False) # Orders data by column values
df.value_counts()                      # Count unique values in a column
df.apply()                             # Apply function to rows/columns
df.pivot_table(values, index, columns) # Creates pivot table from data
```

# Data combining/merging

```python
pd.concat([df1, df2])        # Concatenates multiple DataFrames 
pd.merge(df1, df2, on="key") # Merges two DataFrames on a key column 
df1.join(df2)                # Joins DataFrames on index 
df1.append(df2)              # Appends rows of df2 to df1
```