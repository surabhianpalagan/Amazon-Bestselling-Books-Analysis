
import pandas as pd
import streamlit as st
import plotly.express as px

# PAGE SETTINGS
st.set_page_config(
    page_title="Amazon Books Dashboard",
    page_icon="📚",
    layout="wide"
)

# TITLE
st.title("📚 Amazon Bestselling Books Dashboard")
st.write("Amazon Bestseller Analysis (2009–2019)")

# LOAD DATA
df = pd.read_csv("bestsellers.csv")

# SIDEBAR FILTERS
st.sidebar.header("Filters")

genre = st.sidebar.selectbox(
    "Select Genre",
    ["All"] + sorted(df["Genre"].unique().tolist())
)

year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["Year"].unique().tolist())
)

# APPLY FILTERS
filtered_df = df.copy()

if genre != "All":
    filtered_df = filtered_df[
        filtered_df["Genre"] == genre
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == year
    ]

# SUMMARY STATISTICS
st.header("Key Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Bestseller Entries", len(filtered_df))
col2.metric(
    "Average Rating",
    f"{filtered_df['User Rating'].mean():.2f}"
)
col3.metric(
    "Average Price",
    f"${filtered_df['Price'].mean():.2f}"
)

# TOP AUTHORS
st.header("Top 10 Bestselling Authors")

top_authors = (
    filtered_df["Author"]
    .value_counts()
    .head(10)
)

st.bar_chart(top_authors)

# GENRE COMPARISON
st.header("Fiction vs Nonfiction")

genre_counts = filtered_df["Genre"].value_counts()
st.bar_chart(genre_counts)

# YEARLY PRICE TREND
st.header("Average Book Price by Year")

yearly_prices = (
    filtered_df.groupby("Year")["Price"].mean()
)

st.line_chart(yearly_prices)

# TOP RATED BOOKS
st.header("Top 10 Highest-Rated Books")

top_books = filtered_df.sort_values(
    by=["User Rating", "Reviews"],
    ascending=[False, False]
).head(10)

st.dataframe(
    top_books[
        ["Name", "Author", "User Rating", "Reviews", "Price"]
    ],
    hide_index=True
)

# KEY INSIGHTS
st.header("Key Insights")

if not filtered_df.empty:

    top_author = (
        filtered_df["Author"].value_counts().idxmax()
    )

    highest_rated = filtered_df.loc[
        filtered_df["User Rating"].idxmax()
    ]

    most_reviewed = filtered_df.loc[
        filtered_df["Reviews"].idxmax()
    ]

    st.write("Most Frequent Author:", top_author)
    st.write("Highest-Rated Book:", highest_rated["Name"])
    st.write("Most Reviewed Book:", most_reviewed["Name"])

    correlation = filtered_df["Price"].corr(
        filtered_df["User Rating"]
    )

    if pd.notna(correlation):
        st.write(
            "Price vs Rating Correlation:",
            round(correlation, 3)
        )

# DATA EXPLORER
st.header("Explore All Books")
st.dataframe(filtered_df, hide_index=True)

# DOWNLOAD DATA
st.header("Download Data")

st.download_button(
    label="Download Filtered CSV",
    data=filtered_df.to_csv(index=False),
    file_name="amazon_books_analysis.csv",
    mime="text/csv"
)

st.success("Dashboard loaded successfully!")

# INTERACTIVE DATA VISUALIZATION

st.header("Interactive Book Analysis")

# Price vs Rating
fig1 = px.scatter(
    filtered_df,
    x="Price",
    y="User Rating",
    color="Genre",
    hover_data=["Name", "Author"],
    title="Book Price vs User Rating"
)

st.plotly_chart(fig1, use_container_width=True)

# Reviews vs Rating
fig2 = px.scatter(
    filtered_df,
    x="Reviews",
    y="User Rating",
    color="Genre",
    hover_data=["Name", "Author"],
    title="Customer Reviews vs User Rating"
)

st.plotly_chart(fig2, use_container_width=True)

# Average Rating by Genre
genre_ratings = (
    filtered_df.groupby("Genre", as_index=False)
    ["User Rating"].mean()
)

fig3 = px.bar(
    genre_ratings,
    x="Genre",
    y="User Rating",
    color="Genre",
    title="Average User Rating by Genre"
)

st.plotly_chart(fig3, use_container_width=True)
