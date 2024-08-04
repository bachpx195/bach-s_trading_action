import streamlit as st
from apps.services.get_data_service import GetDataService
from apps.components.chart_overview_component import ChartOverviewComponent
from apps.helpers.datetime_helper import date_name, to_date

MENU_LAYOUT = [1, 1, 1, 7, 2]
CONFIG = {'displayModeBar': False, 'responsive': False}

START_DATE = "2024-01-24"
END_DATE = "2024-02-01"

# START_DATE = "2022-11-01"
# END_DATE = "2023-01-31"

def run():
  st.set_page_config(layout="wide")
  st.write(
      '<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
  st.write(
      '<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
  week_prices, day_prices, hour_prices = GetDataService(
      'LTCUSDT',100, START_DATE, END_DATE, None).run()
  btc_week_prices, btc_day_prices, btc_hour_prices = GetDataService(
      'BTCUSDT', 100, START_DATE, END_DATE, None).run()
  abtc_week_prices, abtc_day_prices, abtc_hour_prices = GetDataService(
      'LTCBTC', 100, START_DATE, END_DATE, None).run()

  for date in day_prices.day.to_list():
    if to_date(START_DATE) <= to_date(date) <= to_date(END_DATE):
      ChartOverviewComponent(
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
      ).run()

if __name__ == "__main__":
    run()
