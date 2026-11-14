
import pandas as pd

# Step 1: Load the Amazon books CSV file
df = pd.read_csv("bestsellers.csv")

# Step 2: Display the first 5 books
print("Amazon Bestselling Books Analysis")
print(df.head())

# Step 3: Find the top 10 highest-rated books

top_books = df.sort_values(
    by="User Rating",
    ascending=False
).head(10)

print("\nTop 10 Highest-Rated Books:")
print(top_books[["Name", "Author", "User Rating"]])

# Step 4: Find the top 10 bestselling authors

top_authors = df["Author"].value_counts().head(10)

print("\nTop 10 Bestselling Authors:")
print(top_authors)

import matplotlib.pyplot as plt

# STEP 5: Average book price
print("\nAverage Book Price:")
print(round(df["Price"].mean(), 2))

# STEP 6: Fiction vs Nonfiction
print("\nBooks by Genre:")
genre_counts = df["Genre"].value_counts()
print(genre_counts)

# STEP 7: Books with the most reviews
print("\nTop 10 Most Reviewed Books:")
most_reviewed = df.sort_values(
    by="Reviews", ascending=False
).head(10)

print(most_reviewed[["Name", "Reviews"]])

# STEP 8: Average rating by genre
print("\nAverage Rating by Genre:")
print(df.groupby("Genre")["User Rating"].mean())

# STEP 9: Average price by year
yearly_prices = df.groupby("Year")["Price"].mean()

print("\nAverage Price by Year:")
print(yearly_prices)

# GRAPH 1: Top 10 Authors
plt.figure(figsize=(10, 5))
top_authors.plot(kind="bar")
plt.title("Top 10 Bestselling Authors")
plt.xlabel("Authors")
plt.ylabel("Bestseller List Appearances")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# GRAPH 2: Fiction vs Nonfiction
plt.figure(figsize=(7, 7))
genre_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Fiction vs Nonfiction")
plt.ylabel("")
plt.show()

# GRAPH 3: Average Price by Year
plt.figure(figsize=(10, 5))
yearly_prices.plot(
    kind="line",
    marker="o"
)
plt.title("Average Book Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Price ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# GRAPH 4: User Ratings Distribution
plt.figure(figsize=(10, 5))
df["User Rating"].plot(
    kind="hist",
    bins=15,
    edgecolor="black"
)
plt.title("Distribution of Book Ratings")
plt.xlabel("User Rating")
plt.ylabel("Number of Entries")
plt.tight_layout()
plt.show()

# GRAPH 5: Price vs User Rating
plt.figure(figsize=(10, 5))
plt.scatter(
    df["Price"],
    df["User Rating"],
    alpha=0.5
)
plt.title("Book Price vs User Rating")
plt.xlabel("Price ($)")
plt.ylabel("User Rating")
plt.tight_layout()
plt.show()

print("\nAnalysis Complete!")
