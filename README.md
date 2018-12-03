# ds-python_examples
Data Science in Python - Example scripts leveraging numpy, pandas, and matplotlib

## Contents
* `mote_carlo_forecast.py` - A Monte Carlo simulation to forecast (poorly) a stock's performance (seriously, *do not* take financial advice from this script or it's output!)
* `saas_company-data_generator.py` - Acme Widget Co. SaaS Data Generator. Supports multiple subscription types.
* `nameage.py` - Estimate a person's age from their first name. Inspired by the FiveThirtyEight article: https://fivethirtyeight.com/features/how-to-tell-someones-age-when-all-you-know-is-her-name/

## Getting Started
After cloning this repo, create a python3 virtual environment and ensure that the *numpy*, *pandas*, *matplotlib*, and *quandl* packages are installed before running each script.

**Step 1** Create a python3 virtual environment. Activate it. Ensure that pip is up to date.
```
ds-python_examples$ python3 -m venv venv
ds-python_examples$ source venv/bin/activate
(venv) ds-python_examples$ pip install -U pip
```

**Step 2** Use pip to install the  *numpy*, *pandas*, *matplotlib*, and *quanl* packages.
```
(venv) ds-python_examples$ pip install -U numpy pandas matplotlib quandl
```

**Step 3** Enjoy the scripts :-)

**Step 4** Remember to deactivate your virtual environment
```
(venv) ds-python_examples$ deactivate
ds-python_examples$
```

