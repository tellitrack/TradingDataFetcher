import yfinance as yf


class YahooFinanceServiceManager:
    def __init__(self, ticker: str):
        print(f"ServiceManager for Yahoo Finance initialized with ticker {ticker}")
        self.ticker = ticker

        self.ticker_base = yf.Ticker(self.ticker)

    def get_stock_price(self, period: str):
        return self.ticker_base.history(period=period)

    def get_historical_data(self, start_date: str, end_date: str):
        return self.ticker_base.history(start=start_date, end=end_date)

    def get_dividends(self):
        return self.ticker_base.dividends

    def get_splits(self):
        return self.ticker_base.splits

    def get_company_info(self):
        return self.ticker_base.info

    def get_financials(self):
        return self.ticker_base.financials

    def get_quarterly_financials(self):
        return self.ticker_base.quarterly_financials

    def get_balance_sheet(self):
        return self.ticker_base.balance_sheet

    def get_quarterly_balance_sheet(self):
        return self.ticker_base.quarterly_balance_sheet

    def get_cashflow(self):
        return self.ticker_base.cashflow

    def get_quarterly_cashflow(self):
        return self.ticker_base.quarterly_cashflow


if __name__ == '__main__':
    ticker = "AAPL"
    start_date = "2024-01-01"
    end_date = "2024-04-02"
    period = "1d"
    manager = YahooFinanceServiceManager(ticker)
    res = manager.get_dividends()
    print(res)
