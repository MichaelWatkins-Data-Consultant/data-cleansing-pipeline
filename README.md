# Data Cleansing Pipeline

## The Problem

Raw business data is almost never clean. Duplicates, missing values,
inconsistent formatting, and bad records silently corrupt reporting
and decision-making. Most teams don't catch these issues until
something breaks — or worse, they never catch them at all.

## The Solution

An automated Python and SQL data cleansing pipeline that:

- Detects and removes duplicate records
- Identifies and fills missing values
- Standardizes text formatting across all columns
- Converts dates to a consistent format
- Removes invalid records (negative sales, bad data)
- Outputs a clean dataset ready for analysis
- Generates a full data quality log documenting every fix

## The Result

| Metric                | Before | After |
| --------------------- | ------ | ----- |
| Total Records         | 10,044 | 9,964 |
| Duplicate Records     | 50     | 0     |
| Missing Values        | 150    | 0     |
| Formatting Issues     | 400+   | 0     |
| Invalid Sales Records | 30     | 0     |

## How It Works

1. `introduce_mess.py` — simulates real-world dirty data
2. `data_cleanser.py` — detects, fixes, and logs all data quality issues

## Sample Log Output

DATE QUALITY REPORT — Generated 2026-04-06
Records before cleansing: 10,044
Records after cleansing: 9,964
Records removed: 80
ISSUES FOUND & FIXED

Duplicates removed: 50
Missing values fixed: 150
Text columns standardized: 8
Date columns converted to standard format
Negative sales records removed: 30

## Tools Used

Python · SQL · SQLite · Pandas

## How To Run

```bash
# Step 1 - Create messy dataset
python3 introduce_mess.py

# Step 2 - Run the cleansing pipeline
python3 data_cleanser.py
```

A clean CSV, clean database, and data quality log will be
generated automatically.
