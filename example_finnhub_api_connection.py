#!/usr/bin/env python3
"""
Example script demonstrating Finnhub API usage.
"""

import os
from dotenv import load_dotenv
import finnhub

# Load environment variables
load_dotenv(dotenv_path=".env", override=True)

def main():
    # Initialize Finnhub client
    api_key = os.getenv('FINNHUB_API_KEY')
    
    if not api_key:
        print("ERROR: FINNHUB_API_KEY not found in .env file")
        print("Please copy .env.example to .env and add your API key")
        return
    
    # Debug: Show that API key was loaded (but don't reveal it)
    print(f"✓ API key loaded (length: {len(api_key)} characters)")
    print(f"✓ API key starts with: {api_key[:4]}..." if len(api_key) > 4 else "✓ API key loaded")
    print()
    
    client = finnhub.Client(api_key=api_key)
    
    # Example 1: Get real-time stock quote
    print("=" * 60)
    print("STOCK QUOTE - AAPL (Apple Inc.)")
    print("=" * 60)
    try:
        quote = client.quote('AAPL')
        print(f"Current Price: ${quote['c']:.2f}")
        print(f"Change: ${quote['d']:.2f} ({quote['dp']:.2f}%)")
        print(f"High: ${quote['h']:.2f}")
        print(f"Low: ${quote['l']:.2f}")
        print(f"Open: ${quote['o']:.2f}")
        print(f"Previous Close: ${quote['pc']:.2f}")
    except Exception as e:
        print(f"Error fetching quote: {e}")
    
    # Example 2: Get company profile
    print("\n" + "=" * 60)
    print("COMPANY PROFILE - AAPL")
    print("=" * 60)
    try:
        profile = client.company_profile2(symbol='AAPL')
        print(f"Name: {profile.get('name', 'N/A')}")
        print(f"Industry: {profile.get('finnhubIndustry', 'N/A')}")
        print(f"Market Cap: ${profile.get('marketCapitalization', 0):,.0f}M")
        print(f"Exchange: {profile.get('exchange', 'N/A')}")
        print(f"Website: {profile.get('weburl', 'N/A')}")
    except Exception as e:
        print(f"Error fetching profile: {e}")
    
    # Example 3: Get market news
    print("\n" + "=" * 60)
    print("LATEST MARKET NEWS")
    print("=" * 60)
    try:
        news = client.general_news('general', min_id=0)
        for i, article in enumerate(news[:3], 1):  # Show top 3 articles
            print(f"\n{i}. {article['headline']}")
            print(f"   Source: {article['source']}")
            print(f"   URL: {article['url']}")
    except Exception as e:
        print(f"Error fetching news: {e}")
    
    print("\n" + "=" * 60)
    print("API test complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
