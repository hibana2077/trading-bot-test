'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-19 23:15:13
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-19 23:30:15
FilePath: \trading-bot-test\lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import pandas_ta as ta

import yfinance as yf

df = yf.download('AAPL', start='2020-01-01', end='2020-03-10')


print(df.ta.macd(fast=12, slow=26, signal=9))