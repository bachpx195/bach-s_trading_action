import streamlit as st
from apps.services.get_data_service import GetDataService
from apps.components.chart_overview_component import ChartOverviewComponent
from apps.helpers.datetime_helper import to_date, next_day, previous_day, to_str

MENU_LAYOUT = [1, 1, 1, 7, 2]
CONFIG = {'displayModeBar': False, 'responsive': False}
MERCHANDISE = "LINK"
OTHER_MERCHANDISES = ["LTC", "DOT"]
SHOW_OTHER_MERCHANDISES = True

def run():
  st.set_page_config(layout="wide")
  st.write(
      '<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
  st.write(
      '<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
  

  # Them *** voi cac ngay phu hop
  LIST_DATE = (
    "2024-10-23",
    "***2024-10-22***",
    "2024-10-21",
    "***2024-10-20***",
    "2024-10-19",
    "***2024-10-18***",
    "2024-10-17",
    "2024-10-16",
    "***2024-10-15***",
    "***2024-10-14***",
    "2024-10-13",
    "***2024-10-12***",
    "***2024-10-11***",
    "***2024-10-10***",
    "2024-10-09",
    "2024-10-08",
    "2024-10-07",
    "***2024-10-06***",
    "***2024-10-05***",
    "***2024-10-04***",
    "***2024-10-03***",
    "2024-10-02",
    "2024-10-01",
  )
  date_select = st.radio(
    "Chọn ngày: ", LIST_DATE)
  date_select = date_select.replace("*", "")
  
  # date_select = st.date_input(label='Chọn ngày')

  START_DATE = previous_day(to_str(date_select))
  END_DATE = next_day(to_str(date_select))

  try:
    week_prices, day_prices, hour_prices = GetDataService(
      f"{MERCHANDISE}USDT", 100, START_DATE, END_DATE, None).run()
    btc_week_prices, btc_day_prices, btc_hour_prices = GetDataService(
      'BTCUSDT', 100, START_DATE, END_DATE, None).run()
    abtc_week_prices, abtc_day_prices, abtc_hour_prices = GetDataService(
      f"{MERCHANDISE}BTC", 100, START_DATE, END_DATE, None).run()
    other_price_data = None
    if SHOW_OTHER_MERCHANDISES:
      other_price_data = {}
      for om in OTHER_MERCHANDISES:
        om_week_prices, om_day_prices, om_hour_prices = GetDataService(
            f"{om}USDT", 100, START_DATE, END_DATE, None).run()
        other_price_data[om] = {
            'week_prices': om_week_prices,
            'day_prices': om_day_prices,
            'hour_prices': om_hour_prices
        }

    for date in day_prices.day.to_list():
      if date == to_str(date_select):
        ChartOverviewComponent(
          MERCHANDISE,
          week_prices,
          day_prices,
          hour_prices,
          date,
          True,
          btc_week_prices,
          btc_day_prices,
          btc_hour_prices,
          abtc_week_prices,
          abtc_day_prices,
          abtc_hour_prices,
          SHOW_OTHER_MERCHANDISES,
          other_price_data
        ).run()
  except IndexError:
    st.write(
      f"Ngay {date_select} chua co data.")
    

if __name__ == "__main__":
    run()
