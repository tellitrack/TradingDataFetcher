from services.YahooFinanceServiceManager.YahooFinance import YahooFinanceServiceManager

ticker = "AAPL"
start_date = "2024-01-01"
end_date = "2024-04-02"
period = "1d"
yf_service = YahooFinanceServiceManager(ticker)


def test_get_stock_price():
    assert yf_service.get_stock_price(period) is not None


def test_get_historical_data():
    assert yf_service.get_historical_data(start_date, end_date) is not None


def test_get_dividends():
    assert yf_service.get_dividends() is not None


def test_get_splits():
    assert yf_service.get_splits() is not None


def test_get_company_info():
    assert yf_service.get_company_info() is not None


def test_get_financials():
    assert yf_service.get_financials() is not None


def test_get_quarterly_financials():
    assert yf_service.get_quarterly_financials() is not None


def test_get_balance_sheet():
    assert yf_service.get_balance_sheet() is not None


def test_get_quarterly_balance_sheet():
    assert yf_service.get_quarterly_balance_sheet() is not None


def test_get_cashflow():
    assert yf_service.get_cashflow() is not None


def test_get_quarterly_cashflow():
    assert yf_service.get_quarterly_cashflow() is not None


if __name__ == '__main__':
    test_get_stock_price()
    test_get_historical_data()
    test_get_dividends()
    test_get_splits()
    test_get_company_info()
    test_get_financials()
    test_get_quarterly_financials()
    test_get_balance_sheet()
    test_get_quarterly_balance_sheet()
    test_get_cashflow()
    test_get_quarterly_cashflow()
