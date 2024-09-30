import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
import urllib
from func import DataAnalyzer, BrazilMapPlotter

sns.set(style='white', palette='muted')
plt.style.use('ggplot')

datetime_columns = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
ecommerce_df = pd.read_csv("https://raw.githubusercontent.com/fikrifaqih80/E-commerce_Dicoding/refs/heads/main/dashboard/df.csv")
ecommerce_df.sort_values(by="order_approved_at", inplace=True)
ecommerce_df.reset_index(inplace=True)

geo_data = pd.read_csv("https://raw.githubusercontent.com/fikrifaqih80/E-commerce_Dicoding/refs/heads/main/dashboard/geolocation.csv")
unique_customer_data = geo_data.drop_duplicates(subset='customer_unique_id')

for column in datetime_columns:
    ecommerce_df[column] = pd.to_datetime(ecommerce_df[column])

earliest_date = ecommerce_df["order_approved_at"].min()
latest_date = ecommerce_df["order_approved_at"].max()

with st.sidebar:
    st.markdown("""
    <style>
    .sidebar-content {
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .sidebar-header {
        font-size: 26px;
        font-weight: bold;
        
        color: #2ECC71;
        margin-bottom: 20px;
    }
    .sidebar-image {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .sidebar-subheader {
        font-size: 18px;
        font-weight: bold;
        color: #F39C12;
        margin-bottom: 10px;
        text-align: center;
    }
    .sidebar-dateinput {
        font-size: 16px;
        margin-bottom: 20px;
    }
    .sidebar-footer {
        font-size: 14px;
        text-align: center;
        color: #808080;
        margin-top: 30px;
    }
    .sidebar-filter-label {
        font-size: 16px;
        color: #34495e;
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-header">📊 E-Commerce Dashboard</div>', unsafe_allow_html=True)
    st.write("Created by: **Fikri Faqih Al Fawwaz**")

    st.markdown('<div class="sidebar-image">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/fikrifaqih80/E-commerce_Dicoding/refs/heads/main/dashboard/logo.png", width=120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-subheader">Filter by Date Range</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-filter-label">Select Date Range</div>', unsafe_allow_html=True)
    date_start, date_end = st.date_input(
        label="",
        value=[earliest_date, latest_date],
        min_value=earliest_date,
        max_value=latest_date
    )

    st.markdown('</div>', unsafe_allow_html=True)

filtered_df = ecommerce_df[(ecommerce_df["order_approved_at"] >= str(date_start)) & 
                           (ecommerce_df["order_approved_at"] <= str(date_end))]

analysis_function = DataAnalyzer(filtered_df)
map_visualization = BrazilMapPlotter(unique_customer_data, plt, mpimg, urllib, st)

daily_orders_data = analysis_function.create_daily_orders_df()
spending_data = analysis_function.create_sum_spend_df()
order_items_data = analysis_function.create_sum_order_items_df()
review_data, most_common_review = analysis_function.review_score_df()
state_data, top_state = analysis_function.create_bystate_df()
status_data, common_status = analysis_function.create_order_status()

st.title("🛒 E-Commerce Insights Dashboard")
st.write("**Explore insights from e-commerce data using interactive visualizations.**")

st.subheader("📅 Daily Orders Delivered")
column1, column2 = st.columns(2)

with column1:
    total_orders = daily_orders_data["order_count"].sum()
    st.markdown(f"Total Orders: **{total_orders}**")

with column2:
    total_revenue = daily_orders_data["revenue"].sum()
    st.markdown(f"Total Revenue: **{total_revenue}**")

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    x=daily_orders_data["order_approved_at"],
    y=daily_orders_data["order_count"],
    marker="o",
    linewidth=2,
    color="#2ECC71"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

st.subheader("💰 Customer Spending Overview")
column1, column2 = st.columns(2)

with column1:
    total_spent = spending_data["total_spend"].sum()
    st.markdown(f"Total Spending: **{total_spent}**")

with column2:
    average_spending = spending_data["total_spend"].mean()
    st.markdown(f"Average Spending: **{average_spending}**")

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    data=spending_data,
    x="order_approved_at",
    y="total_spend",
    marker="o",
    linewidth=2,
    color="#F39C12"
)

ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

st.subheader("📦 Product Orders Overview")
column1, column2 = st.columns(2)

with column1:
    total_products = order_items_data["product_count"].sum()
    st.markdown(f"Total Products: **{total_products}**")

with column2:
    average_products = order_items_data["product_count"].mean()
    st.markdown(f"Average Products: **{average_products}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 10))

sns.barplot(x="product_count", y="product_category_name_english", data=order_items_data.head(5), palette="Set2", ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=12)
ax[0].set_title("Top Products Sold", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=10)
ax[0].tick_params(axis ='x', labelsize=10)

sns.barplot(x="product_count", y="product_category_name_english", data=order_items_data.sort_values(by="product_count", ascending=True).head(5), palette="Set3", ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=12)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Fewest Products Sold", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=10)
ax[1].tick_params(axis='x', labelsize=10)

st.pyplot(fig)

st.subheader("⭐ Review Score Overview")
column1, column2 = st.columns(2)

with column1:
    average_review = review_data.mean()
    st.markdown(f"Average Review Score: **{average_review:.2f}**")

with column2:
    common_review = review_data.value_counts().idxmax()
    st.markdown(f"Most Common Review Score: **{common_review}**")

fig, ax = plt.subplots(figsize=(12, 6))
colors = sns.color_palette("husl", len(review_data))

sns.barplot(x=review_data.index,
            y=review_data.values,
            order=review_data.index,
            palette=colors)

plt.title("Customer Review Scores for Service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for i, value in enumerate(review_data.values):
    ax.text(i, value + 5, str(value), ha='center', va='bottom', fontsize=12, color='black')

st.pyplot(fig)

st.subheader("🌍 Customer Demographics")
tab1, tab2 = st.tabs(["By State", "Geolocation"])

with tab1:
    top_state = state_data.customer_state.value_counts().index[0]
    st.markdown(f"Most Common State: **{top_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state_data.customer_state.value_counts().index,
                y=state_data.customer_count.values, 
                data=state_data,
                palette="Paired"
                )

    plt.title("Number of Customers by State", fontsize=15)
    plt.xlabel("State")
    plt.ylabel("Number of Customers")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab2:
    map_visualization.plot()

    with st.expander("See Explanation"):
        st.write('The data shows that most customers are located in the southeast and southern regions, particularly in major cities like São Paulo and Rio de Janeiro.')

st.markdown("""
    <hr>
    <p style="text-align: center; color: #808080;">© 2024 Fikri Faqih Al Fawwaz</p>
""", unsafe_allow_html=True)
