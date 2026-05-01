import streamlit as st

# 1. Title + Description
st.title("Simple Sales Dashboard")
st.write("This dashboard shows monthly sales data.")

# 2. Selectbox with months
months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month", months)

# 3. Static dictionary of sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# 4. Display selected month's sales
st.metric(label=f"Sales in {selected_month}", value=sales[selected_month])

# OR you can use:
# st.write(f"Sales in {selected_month}: {sales[selected_month]}")

# 5. Bar chart
st.bar_chart(list(sales.values()))