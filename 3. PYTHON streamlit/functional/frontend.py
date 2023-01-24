import pandas as pd
import streamlit as st

from functional.backend import price_coin


def interface():
    dice_type = st.sidebar.selectbox("Select an asset", ("BTC", "ETH", "ATOM", "SOL", "XLM"))

    date_from, date_to = st.sidebar.columns(2)
    date_from = date_from.date_input("Date from")
    date_to = date_to.date_input("Date to")

    st.write(f"""Are you tracking the coin: {dice_type}
From {date_from} to {date_to}""")

    try:
        all_info = price_coin(dice_type, date_from, date_to)
        df = pd.DataFrame(all_info[1], all_info[0])
        st.bar_chart(df)

    except:
        st.write("Вы выбрали недоступную дату, поменяйте!")
