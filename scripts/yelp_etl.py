import pandas as pd
import json
import os

# === CONFIG ===
DATA_FOLDER = "data"
EXPORT_FOLDER = "export"
MAX_REVIEWS = 50000  # For speed — adjust as needed
FOOD_KEYWORDS = ["pizza", "burger", "ramen", "taco", "sushi", "salad", "burrito", "pasta", "fries", "steak"]

# === Ensure export folder exists ===
os.makedirs(EXPORT_FOLDER, exist_ok=True)

# === Step 1: Load business.json and filter restaurants ===
print("📥 Loading business.json...")
business_data = []
with open(f"{DATA_FOLDER}/business.json", encoding="utf8") as f:
    for line in f:
        business_data.append(json.loads(line))

business_df = pd.DataFrame(business_data)

# Filter to restaurants
restaurants_df = business_df[
    business_df['categories'].notna() &
    business_df['categories'].str.contains("Restaurant", case=False, na=False)
][['business_id', 'name', 'city', 'stars', 'review_count', 'categories']]

print(f"✅ Filtered {len(restaurants_df)} restaurants")

# === Step 2: Load review.json and limit rows ===
print(f"📥 Loading first {MAX_REVIEWS} reviews from review.json...")
review_data = []
with open(f"{DATA_FOLDER}/review.json", encoding="utf8") as f:
    for i, line in enumerate(f):
        if i >= MAX_REVIEWS:
            break
        review_data.append(json.loads(line))

review_df = pd.DataFrame(review_data)
print(f"✅ Loaded {len(review_df)} reviews")

# === Step 3: Merge reviews + business info ===
print("🔗 Merging reviews with restaurant info...")
merged_df = review_df.merge(restaurants_df, on="business_id")

# === Step 4: Extract food keyword mentions ===
print("🔍 Identifying dish mentions...")
def extract_dish(text):
    text = text.lower()
    for word in FOOD_KEYWORDS:
        if word in text:
            return word
    return None

merged_df["mentioned_dish"] = merged_df["text"].apply(extract_dish)
dishes_df = merged_df[merged_df["mentioned_dish"].notna()]

print(f"✅ Found {len(dishes_df)} reviews mentioning food keywords")

# === Step 5: Export for dashboarding / Power BI ===
output_path = f"{EXPORT_FOLDER}/yelp_dish_mentions.csv"
dishes_df.to_csv(output_path, index=False)
print(f"📁 Saved cleaned data to: {output_path}")
