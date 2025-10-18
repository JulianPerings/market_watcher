# Market Watcher - Finnhub API

A simple Python repository for exploring the Finnhub market data API.

## Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

1. Sign up for a free API key at [Finnhub.io](https://finnhub.io/)
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add your API key to `.env`:
   ```
   FINNHUB_API_KEY=your_actual_api_key_here
   ```

## Usage

Run the example script to test the API:

```bash
python example.py
```

## Example Output

(venv) julian@BCWMC3238421057:~/repos/market_watcher$ python3 example.py 
============================================================
STOCK QUOTE - AAPL (Apple Inc.)
============================================================
Current Price: $252.29
Change: $4.84 (1.96%)
High: $253.38
Low: $247.27
Open: $248.02
Previous Close: $247.45

============================================================
COMPANY PROFILE - AAPL
============================================================
Name: Apple Inc
Industry: Technology
Market Cap: $3,744,082M
Exchange: NASDAQ NMS - GLOBAL MARKET
Website: https://www.apple.com/

============================================================
LATEST MARKET NEWS
============================================================

1. The stereotype is 'that women want or need relationships more,' but data shows it's men who are more likely to rush down the aisle
   Source: CNBC
   URL: https://www.cnbc.com/2025/10/18/new-data-men-are-more-likely-to-rush-down-the-aislenot-women.html

2. ‘My family is having a crisis’: My mom added my brother to her mortgage. He stopped paying. How does she get him off it?
   Source: MarketWatch
   URL: https://www.marketwatch.com/story/my-family-is-having-a-crisis-my-mom-added-my-brother-to-her-mortgage-he-stopped-paying-how-does-she-get-him-off-it-960f55b0

3. The No. 1 travel destination of 2026 is in the U.S., says new report
   Source: CNBC
   URL: https://www.cnbc.com/2025/10/18/the-no-1-travel-destination-of-2026-is-in-the-us-says-new-report.html

============================================================
API test complete!
=========================================================
## Available API Endpoints

The Finnhub API provides access to:

- **Stock Quotes**: Real-time and historical stock prices
- **Company Profile**: Company information and financials
- **Market News**: Financial news and sentiment analysis
- **Technical Indicators**: Various technical analysis indicators
- **Economic Data**: Economic calendars and indicators
- **Crypto Data**: Cryptocurrency prices and exchanges

## Example Scripts

### `example.py`
Basic example demonstrating:
- Fetching real-time stock quotes
- Getting company profile information
- Retrieving market news

## Resources

- [Finnhub API Documentation](https://finnhub.io/docs/api)
- [Python Client GitHub](https://github.com/Finnhub-Stock-API/finnhub-python)

## License

MIT
