# 🚀 Market Watcher - Finnhub API

> A comprehensive Python toolkit for exploring the Finnhub market data API with real-time stock quotes, company profiles, financial news, and AI-powered investment analysis.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Finnhub-API-green.svg" alt="Finnhub API">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4-yellow.svg" alt="OpenAI GPT-4">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📊 Example Output](#-example-output)
- [📚 Resources](#-resources)

---

## ✨ Features

- **📈 Real-time Stock Quotes** - Live stock prices and market data
- **🏢 Company Profiles** - Detailed company information and financials
- **📰 Market News** - Latest financial news and sentiment analysis
- **🤖 AI Investment Advisor** - GPT-4 powered investment recommendations
- **💹 Technical Indicators** - Market trend analysis tools
- **📊 Economic Data** - Economic calendars and indicators
- **₿ Crypto Support** - Cryptocurrency prices and exchanges
- **🔒 Secure** - Environment-based API key management

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [Finnhub.io](https://finnhub.io/) account (free tier available)
- [OpenAI](https://platform.openai.com/) account (for AI features)

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/JulianPerings/market_watcher.git
cd market_watcher

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys:
# FINNHUB_API_KEY=your_finnhub_key_here
# OPENAI_API_KEY=your_openai_key_here
```

### Basic Usage

```bash
# Test the Finnhub API connection
python3 example_finnhub_api_connection.py

# Run AI-powered investment analysis
python3 openai_market_advisor.py
```

---

## 📊 Example Output

### Finnhub API Connection (`example_finnhub_api_connection.py`)
```bash
(venv) user@machine:~/market_watcher$ python3 example_finnhub_api_connection.py

============================================================
📈 STOCK QUOTE - AAPL (Apple Inc.)
============================================================
Current Price: $252.29
Change: $4.84 (1.96%)
High: $253.38
Low: $247.27
Open: $248.02
Previous Close: $247.45

============================================================
🏢 COMPANY PROFILE - AAPL
============================================================
Name: Apple Inc
Industry: Technology
Market Cap: $3,744,082M
Exchange: NASDAQ NMS - GLOBAL MARKET
Website: https://www.apple.com/

============================================================
📰 LATEST MARKET NEWS
============================================================
1. The stereotype is 'that women want or need relationships more,' but data shows it's men who are more likely to rush down the aisle
   Source: CNBC
   URL: https://www.cnbc.com/2025/10/18/new-data-men-are-more-likely-to-rush-down-the-aislenot-women.html
...
============================================================
✅ API test complete!
============================================================
```

### AI Investment Advisor (`openai_market_advisor.py`)
```bash
(venv) user@machine:~/market_watcher$ python3 openai_market_advisor.py

🚀 OpenAI Market Advisor
============================================================
📊 Using prebuilt Apple data example...

🧠 APPLE INC. ANALYSIS
============================================================
📊 Analysis for: AAPL
⏰ Generated: 2025-10-19 16:25:54

OVERALL RECOMMENDATION: BUY
CONFIDENCE LEVEL: High

KEY ARGUMENTS:
1. Strong Q4 earnings: Apple's recent earnings report showed a 15% YoY increase in iPhone sales, suggesting strong product demand and financial health.
2. Technological advancements: The announcement of new AI features in the upcoming iOS update indicates Apple's continuous innovation and potential for future growth.
3. Strategic partnerships: The partnership with a major automotive manufacturer for CarPlay expansion shows Apple's ability to diversify its revenue streams and expand its market presence.
4. Dominant market position: As a leader in the technology sector and consumer electronics, Apple has a proven track record of delivering quality products and maintaining customer loyalty.

RISK FACTORS:
1. Market saturation: With many of its products, particularly the iPhone, Apple faces the challenge of market saturation which could limit growth.
2. Dependence on certain products: A significant portion of Apple's revenue comes from the iPhone. If iPhone sales were to decline significantly, it could have a substantial impact on the company's overall performance.
3. Regulatory risk: As a multinational tech company, Apple faces regulatory risks in various jurisdictions, which could affect its operations and profitability.

TIME HORIZON: Long-term

BRIEF SUMMARY: Given Apple's strong Q4 earnings, continuous innovation, strategic partnerships, and market dominance, a 'Buy' recommendation is suggested with high confidence. Despite potential risks such as market saturation, over-dependence on iPhone sales, and regulatory challenges, Apple's diversified revenue streams and forward-looking strategies show promising potential for long-term investment.

✅ Analysis complete!
```

---

## 📚 Resources

- 📖 **[Finnhub API Documentation](https://finnhub.io/docs/api)** - Complete API reference
- 💻 **[Python Client GitHub](https://github.com/Finnhub-Stock-API/finnhub-python)** - Official Python SDK
- 🤖 **[OpenAI Platform](https://platform.openai.com/)** - Get your OpenAI API key
- 🚀 **[Finnhub.io](https://finnhub.io/)** - Sign up for your free API key

---

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the financial markets community**

[⭐ Star this repo if you found it helpful!](https://github.com/JulianPerings/market_watcher)

</div>
