# MIT License
# 
# Copyright (c) 2018 Michael DeFelice
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np, pandas as pd
import quandl

from matplotlib.ticker import FuncFormatter, MultipleLocator
import matplotlib.pyplot as plt
plt.style.use ('ggplot')

# For better feeds, create an account on quandl.com and include your API key in the call
df = quandl.get ('WIKI/AAPL', start_date = '2017-01-01', rows = 250)

# Isolate the close price column
s = df['Close'].rename ('AAPL_Close_Price')
end_price = s.iloc[-1]

# This may be helpful ... mostly a placeholder to store the formula to calculate CAGR with less than a year's data
cagr = ((end_price / float (s.iloc[0])) ** (365/float (s.shape[0]))) - 1

# Daily changes as percentages
changes = s.pct_change ()
mu = changes.mean ()
vD = changes.std ()

# Create an array of 10000 random walks - each with 90 steps
k = np.cumprod (1 + np.random.normal (mu, vD, (10000,90)), 1) * end_price

# The last step as an array. In this case, useful to answer the question: "In 90 days, where could this go?"
l = k[:, -1]

# Plot
fig, ax = plt.subplots (2, 1, figsize = (11, 8.5))
ax[0].plot (k.T, linewidth = 0.5)
ax[0].set_title ("Forward Modeling; N = {:,}; {:,} Walks; {:,} Periods".format (len (s), *k.shape))
ax[0].get_yaxis ().set_major_formatter (FuncFormatter (lambda a, b: '${:,.0f}'.format (a * 1e-0)))
ax[0].set_xlim (0, k.T.shape[0])

# Add a dotted line to trace the mean across the walks
ax[0].plot ([_.mean () for _ in k.T], color = 'k', linewidth = 1, linestyle = ':', label = 'Expected Value')

# Annotate
ax[0].annotate ('CAGR:  {}\nvD:    {}\nmu:    {}'.format (round (cagr, 8), round (vD, 8), round (mu, 8)), xy = (0, 45), xycoords = 'axes pixels', xytext = (4, 0), textcoords = 'offset points', ha = 'left', va = 'center', fontsize = 8, family = 'monospace', fontweight = 'normal', bbox = {'facecolor': 'white', 'edgecolor': 'none', 'pad': 4,})

# What does the last stew look like across all walks?
ax[1].hist (l, bins = 100)
ax[1].set_title ("Day {} (All Walks)".format (k.shape[1]))
ax[1].get_xaxis ().set_major_formatter (FuncFormatter (lambda a, b: '${:,.0f}'.format (a * 1e-0)))

plt.show ()

