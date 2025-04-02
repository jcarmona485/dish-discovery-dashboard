-- Load CSV into SQL Table (example for SQLite / PostgreSQL)
CREATE TABLE dishes (
    dish_name TEXT,
    restaurant TEXT,
    city TEXT,
    rating REAL,
    price REAL,
    diet TEXT
);

-- Sample Query 1: Top rated dish per city
SELECT city, dish_name, MAX(rating) as top_rating
FROM dishes
GROUP BY city;

-- Sample Query 2: Average rating by diet type
SELECT diet, ROUND(AVG(rating), 2) as avg_rating
FROM dishes
GROUP BY diet
ORDER BY avg_rating DESC;

-- Sample Query 3: Best value dishes (high rating, low price)
SELECT dish_name, rating, price
FROM dishes
WHERE rating >= 4.4 AND price <= 13
ORDER BY rating DESC;
