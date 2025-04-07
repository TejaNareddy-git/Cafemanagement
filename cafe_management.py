import streamlit as st

# Define the menu
Menu = {
    "Pizza": 160,
    "Burger": 100,
    "Maggie": 50,
    "Hot Coffee": 40,
    "Cold Coffee": 30,
}

st.title("Cafe Management System")
st.subheader("Menu")

st.table([{"Item": item, "Price (₹)": price} for item, price in Menu.items()])

# Initialize session state for order management
if 'order' not in st.session_state:
    st.session_state.order = []

# Ordering system (this should always be visible)
selected_item = st.selectbox("Select an item to order:", list(Menu.keys()))

if st.button("Add to Order"):
    st.session_state.order.append(selected_item)
    st.success(f"{selected_item} added to your order!")

# Display current order
if st.session_state.order:
    st.subheader("Your Order")
    order_summary = {item: st.session_state.order.count(item) for item in set(st.session_state.order)}
    total_amount = sum(Menu[item] * qty for item, qty in order_summary.items())

    st.table([
        {"Item": item, "Quantity": qty, "Price (₹)": Menu[item] * qty}
        for item, qty in order_summary.items()
    ])
    st.write(f"Total Amount: ₹{total_amount}")

    if st.button("Confirm Order"):
        st.success("Order confirmed! Thank you for your purchase.")
        st.session_state.order = []