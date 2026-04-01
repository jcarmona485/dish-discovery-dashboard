#  Dish Discovery Dashboard (Yelp Open Dataset)

This project is a beginner-friendly but fully functional data pipeline built using real Yelp review data. The goal was to extract food-related insights — specifically about dishes mentioned in restaurant reviews — and turn that into something meaningful through analysis and visualization.

I built this to practice real-world data tasks like working with large JSON files, cleaning messy text, aggregating insights, and presenting them in a clear way. It simulates how a data analyst or engineer might approach solving a practical business problem.

---

## What This Project Does

- Loads real Yelp data (`business.json` and `review.json`)
- Filters reviews to only include **restaurant-related businesses**
- Extracts reviews that mention specific dishes (like pizza, sushi, burger, etc.)
- Merges review and business data into a clean dataset
- Calculates:
  - Most mentioned dishes
  - Highest-rated dishes
  - Dish ratings by city
- Visualizes results using bar charts and heatmaps
- Exports cleaned CSVs for Power BI or SQL use

---

## Tools Used

- Python (Pandas, Matplotlib, Seaborn)
- JSON file processing
- Jupyter Notebook
- Basic SQL-style grouping and joins
- Power BI (optional export-ready files)

---

## Format
-Top dishes
  >data (Raw Json files)
    -business.json
    -review.json
    
  >export (Clean CSV's for analysis)
    -dish_summary_powerbi.csv
    -yelp_dish_mentions.csv

  >scripts (ETL pipeline)
    -yelp_etl.py

  >sql (optional SQL queries)
    -dish_queries.sql

  >dish_analysis.ipynb (main analysis notebook)

  >README.md (What you are reading now)
---

## How to Run It

1. Download the [Yelp Open Dataset](https://www.yelp.com/dataset/download)
2. Place `business.json` and `review.json` inside the `data/` folder
3. Run the ETL script:
   ```bash
   python scripts/yelp_etl.py

---

## Why I Built This
I wanted to challenge myself to work with larger, real-world data and build a complete workflow — not just look at clean CSVs. This project helped me understand the importance of filtering, merging, and telling a clear story with data.

---

## About Me
I’m learning data analysis and data engineering, and I’m excited about solving real problems with data. This is one of my first big end-to-end projects — feedback is always welcome!
