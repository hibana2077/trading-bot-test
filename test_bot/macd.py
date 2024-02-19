'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-19 22:59:30
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-19 23:36:07
FilePath: \trading-bot-test\test_bot\macd.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import pandas_ta as ta
from datetime import datetime

from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy

class MACD(Strategy):
    def initialize(self, my_custom_parameter=True):
        self.sleeptime = "1D"
    def on_trading_iteration(self):
        bars = self.get_historical_prices("WBC.AX", 60, "day")
        df = bars.df
        temp = df.ta.macd(fast=12, slow=26, signal=9)
        df['macd'] = temp['MACD_12_26_9']
        df['macd_signal'] = temp['MACDs_12_26_9']
        df['macd_hist'] = temp['MACDh_12_26_9']
        buy = df['macd'].iloc[-1] > df['macd_signal'].iloc[-1] and df['macd'].iloc[-2] < df['macd_signal'].iloc[-2] and df['macd_hist'].iloc[-1] > 0
        sell = df['macd'].iloc[-1] < df['macd_signal'].iloc[-1] and df['macd'].iloc[-2] > df['macd_signal'].iloc[-2] and df['macd_hist'].iloc[-1] < 0
        quantity = self.portfolio_value // df['close'].iloc[-1]
        if buy:
            order = self.create_order("WBC.AX", quantity, "buy")
            self.submit_order(order)
        if sell:
            self.sell_all()

# Pick the dates that you want to start and end your backtest
# and the allocated budget
backtesting_start = datetime(2020, 11, 1)
backtesting_end = datetime(2023, 12, 31)

# Run the backtest
MACD.backtest(
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
)