import pandas as pd
import sqlite3
from datetime import datetime

# ============================================
# STEP 1: LOAD THE RAW DATA
# ============================================
print("Loading raw data...")
df = pd.read_csv('superstore_messy.csv', encoding='latin1')

# Track quality issues found
log = []
original_count = len(df)

# ============================================
# STEP 2: REMOVE DUPLICATE ROWS
# ============================================
duplicates = df.duplicated().sum()
df = df.drop_duplicates()
log.append(f"Duplicates removed: {duplicates}")
print(f"✓ Duplicates removed: {duplicates}")

# ============================================
# STEP 3: FIX MISSING VALUES
# ============================================
missing_before = df.isnull().sum().sum()
df['Postal Code'] = df['Postal Code'].fillna('UNKNOWN')
df['Region'] = df['Region'].fillna('UNKNOWN')
missing_after = df.isnull().sum().sum()
log.append(f"Missing values fixed: {missing_before - missing_after}")
print(f"✓ Missing values fixed: {missing_before - missing_after}")

# ============================================
# STEP 4: STANDARDIZE TEXT FORMATTING
# ============================================
text_columns = ['Ship Mode', 'Segment', 'Country', 'City', 
                'State', 'Region', 'Category', 'Sub-Category']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()
log.append(f"Text columns standardized: {len(text_columns)}")
print(f"✓ Text columns standardized: {len(text_columns)}")

# ============================================
# STEP 5: FIX DATE FORMATTING
# ============================================
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
log.append("Date columns converted to standard format")
print(f"✓ Date columns standardized")

# ============================================
# STEP 6: REMOVE NEGATIVE SALES
# ============================================
negative_sales = (df['Sales'] < 0).sum()
df = df[df['Sales'] >= 0]
log.append(f"Negative sales records removed: {negative_sales}")
print(f"✓ Negative sales records removed: {negative_sales}")

# ============================================
# STEP 7: SAVE CLEAN DATA TO CSV AND DATABASE
# ============================================
df.to_csv('superstore_clean.csv', index=False)

conn = sqlite3.connect('superstore_clean.db')
df.to_sql('clean_sales', conn, if_exists='replace', index=False)
conn.close()

print(f"✓ Clean data saved to superstore_clean.csv and superstore_clean.db")

# ============================================
# STEP 8: GENERATE THE DATA QUALITY LOG
# ============================================
report_date = datetime.now().strftime('%Y-%m-%d')
log_filename = f'data_quality_log_{report_date}.txt'

with open(log_filename, 'w') as f:
    f.write("=" * 60 + "\n")
    f.write(f"  DATA QUALITY REPORT — Generated {report_date}\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Records before cleansing: {original_count}\n")
    f.write(f"Records after cleansing:  {len(df)}\n")
    f.write(f"Records removed:          {original_count - len(df)}\n\n")
    f.write("ISSUES FOUND & FIXED\n")
    f.write("-" * 60 + "\n")
    for item in log:
        f.write(f"• {item}\n")

print(f"\n✓ Data quality log saved: {log_filename}")
print(f"\nDone! {original_count} records in → {len(df)} clean records out.")