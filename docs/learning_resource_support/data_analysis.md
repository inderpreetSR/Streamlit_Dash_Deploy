# Data Analysis (Pandas & Domain) Learning Resource

## Overview
Data analysis involves inspecting, cleaning, transforming, and modeling data to discover useful information. Pandas is the primary Python library for data analysis.

## Key Concepts & Glossary
- **DataFrame**: 2D labeled data structure
- **Series**: 1D labeled array
- **Indexing**: Selecting rows/columns
- **GroupBy**: Aggregation by category
- **Missing Data**: Handling NaN/null values

## Syntax & Examples
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.info()
df['col'].mean()
df.groupby('category').sum()
```

## Common Use Cases
- Data cleaning
- Exploratory data analysis (EDA)
- Feature engineering
- Statistical summaries

## Setup & Usage
```bash
pip install pandas
```

## Best Practices
- Always inspect data with `df.info()` and `df.describe()`
- Handle missing values early
- Use vectorized operations for performance

## External Learning Links
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Pandas Tutorials (YouTube)](https://www.youtube.com/results?search_query=pandas+tutorial)
- [Awesome Pandas](https://github.com/tommyod/awesome-pandas)

## How Data Analysis is Used in This Project
- Loading, cleaning, and analyzing financial/loan data
- Used in `src/utils/data_loader.py` and `src/utils/data_analyzer.py` 

## Core Concepts Used in This Project
- Used Pandas for data loading, cleaning, and analysis.
- Chosen for its power, flexibility, and community support.
- Used DataFrames, groupby, and vectorized operations.

## Ignored/Alternative Concepts
- Not used: Dask, Vaex, Polars, or SQL-based analysis.
- Reason: Pandas is the standard for in-memory data analysis in Python.

## Other Concepts You Could Use
- Dask for out-of-core/big data
- Polars for faster, multi-threaded analysis
- Integration with scikit-learn for ML

## Technology Foundations
- Built on NumPy and C extensions for speed.

## Advantages & Disadvantages
**Advantages:**
- Extremely flexible and powerful
- Rich ecosystem and documentation
- Great for EDA and prototyping

**Disadvantages:**
- Memory-bound (not for huge datasets)
- Can be slow for very large data
- API can be complex for beginners 

## Project Keywords Used
- pandas
- pd.read_csv
- DataFrame
- df.info
- df.describe
- df.groupby
- df['col']
- Data cleaning
- Feature engineering
- Exploratory Data Analysis (EDA) 