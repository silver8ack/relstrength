import stockinator as st
import datetime

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=400)
#end_date.strftime('%Y-%m-%d')

tickers = st.get_tickers()

just_tickers = []
for t in tickers:
    just_tickers.append(t['symbol'])


def get_stock_data(tickers, start=None, end=None, interval='1d', period=None):
    return yf.download(
        tickers=' '.join(tickers),
        start=start,
        end=end,
        period=period,
        interval=interval,
        group_by="ticker",
        auto_adjust=False,
        threads=True
    )

def get_history(ticker=None, start_date=None, end_date=None):
    url = f"https://api.nasdaq.com/api/quote/{ticker}/chart?assetclass=stocks&fromdate={start_date}&todate={end_date}"
    headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    try:
        return resp.json()['data']
    except:
        pass

def get_data(t):
  d = get_history(t['symbol'], start_date='2022-01-01', end_date='2023-02-14')
  return d