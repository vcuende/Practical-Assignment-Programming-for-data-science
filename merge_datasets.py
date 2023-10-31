import pandas as pd

# 2 class files, 1 our files
opt = 2

if opt == 1:
    # Load each dataset
    df1 = pd.read_csv('./files/cash/usdollar.csv')
    df2 = pd.read_csv('files/corporate bonds/ishares-global-corporate-bond-$.csv')
    df3 = pd.read_csv('files/gold/spdr-gold-trust.csv')
    df4 = pd.read_csv('files/public bonds/db-x-trackers-ii-global-sovereign-5.csv')
    df5 = pd.read_csv('files/stocks/amundi-msci-wrld-ae-c.csv')

else:

    df1 = pd.read_csv('./assets_historical_prices/usdollar_investing.csv', delimiter="\t")
    df2 = pd.read_csv('./assets_historical_prices/ishares-global-corporate-bond-$_investing.csv', delimiter="\t")
    df3 = pd.read_csv('./assets_historical_prices/spdr-gold-trust_investing.csv', delimiter="\t")
    df4 = pd.read_csv('./assets_historical_prices/db-x-trackers-ii-global-sovereign-5_investing.csv', delimiter="\t")
    df5 = pd.read_csv('./assets_historical_prices/amundi-msci-wrld-ae-c_investing.csv', delimiter="\t")

df1['source'] = 'df1'
df2['source'] = 'df2'
df3['source'] = 'df3'
df4['source'] = 'df4'
df5['source'] = 'df5'

date_col = "Date" if opt == 2 else "date"
price_col = "Price" if opt == 2 else "price"

# Merge datasets on the common date column
merged_df = pd.concat([df1, df2, df3, df4, df5]).reset_index(drop=True)

# Convert date column to a common format
merged_df[date_col] = pd.to_datetime(merged_df[date_col], errors='coerce')

# Fill in missing values with -1
merged_df[price_col] = merged_df[price_col].fillna(-1)

# Create separate columns for each value column from the original datasets
merged_df['CA'] = merged_df[price_col].where(merged_df['source'] == 'df1')
merged_df['CB'] = merged_df[price_col].where(merged_df['source'] == 'df2')
merged_df['GO'] = merged_df[price_col].where(merged_df['source'] == 'df3')
merged_df['PB'] = merged_df[price_col].where(merged_df['source'] == 'df4')
merged_df['ST'] = merged_df[price_col].where(merged_df['source'] == 'df5')

# Group by date and sum the value columns
grouped_df = merged_df.groupby(date_col).agg({
    'CA': 'sum',
    'CB': 'sum',
    'GO': 'sum',
    'PB': 'sum',
    'ST': 'sum'
}).reset_index()

# Save the merged and aggregated dataset
file_name = "all_2.csv" if opt == 2 else "all.csv"
if opt == 2:
    grouped_df.rename(columns = {"Date": "date"}, inplace=True)
grouped_df.to_csv(f'./files/all/{file_name}', index=False)