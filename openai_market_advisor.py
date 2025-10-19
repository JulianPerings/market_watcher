#!/usr/bin/env python3
"""
OpenAI Market Advisor - Investment Analysis Tool

This script helps analyze market data and provides investment recommendations using OpenAI.

SETUP:
1. Install dependencies: pip install -r requirements.txt
2. Add your API key to .env: OPENAI_API_KEY=your_key_here
3. Run: python3 openai_market_advisor.py

INPUT METHODS (choose one):
1. Prebuilt string example (uncomment the example you want to use)
2. Use data from example.py (commented out below)
3. Use data from a file (commented out below)
"""

import os
import json
import argparse
from datetime import datetime
from dotenv import load_dotenv
import openai
import subprocess

# Load environment variables
load_dotenv(dotenv_path=".env", override=True)

def analyze_investment_data(market_data_text, symbol="AAPL"):
    """
    Analyze market data using OpenAI and provide investment recommendation.

    Args:
        market_data_text (str): The market data to analyze
        symbol (str): Stock symbol being analyzed

    Returns:
        str: AI analysis and recommendation
    """
    openai_key = os.getenv('OPENAI_API_KEY')
    if not openai_key:
        return "❌ OPENAI_API_KEY not found in .env file. Please add it and try again."

    try:
        # Initialize OpenAI client (OpenAI v2.x style)
        client = openai.OpenAI(api_key=openai_key)

        prompt = f"""
        You are a professional investment advisor. Please analyze the following market data for {symbol}
        and provide a clear investment recommendation.

        Market Data:
        {market_data_text}

        Please provide:
        1. OVERALL RECOMMENDATION: BUY, HOLD, or SELL
        2. CONFIDENCE LEVEL: High/Medium/Low
        3. KEY ARGUMENTS (3-4 main points)
        4. RISK FACTORS (2-3 potential concerns)
        5. TIME HORIZON: Short-term/Medium-term/Long-term
        6. BRIEF SUMMARY (2-3 sentences)

        Format your response clearly with headings and bullet points.
        """

        # Updated API call for OpenAI v2.x
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert investment advisor providing clear, actionable recommendations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        # Updated response access for OpenAI v2.x
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error analyzing with OpenAI: {e}"

def get_data_from_example_py():
    """
    Simple method: Run example_finnhub_api_connection.py and capture all its output as a string.
    This is the easiest way to use example.py data.
    """
    try:
        # Run example_finnhub_api_connection.py and capture all output
        result = subprocess.run(
            ['python3', 'example_finnhub_api_connection.py'],
            capture_output=True,
            text=True,
            cwd='.'  # Current directory
        )

        if result.returncode == 0:
            # Return all the output as a string
            return result.stdout
        else:
            return f"❌ Error running example_finnhub_api_connection.py (exit code: {result.returncode}):\n{result.stderr}"

    except FileNotFoundError:
        return "❌ example_finnhub_api_connection.py not found in current directory"
    except Exception as e:
        return f"❌ Error running example_finnhub_api_connection.py: {e}"

def display_analysis(title, analysis, symbol="AAPL"):
    """Display the analysis in a formatted way"""
    print(f"\n🧠 {title}")
    print("=" * 60)
    print(f"📊 Analysis for: {symbol}")
    print(f"⏰ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + analysis)

def main():
    parser = argparse.ArgumentParser(description="OpenAI Market Advisor")
    parser.add_argument('--symbol', default='AAPL', help='Stock symbol to analyze')
    args = parser.parse_args()

    print("🚀 OpenAI Market Advisor")
    print("=" * 60)

    # ============================================================================
    # INPUT METHOD 1: PREBUILT STRING EXAMPLE (RECOMMENDED FOR TESTING)
    # ============================================================================

    # Example 1: Apple data (from example.py format)
    
    market_data = """
    Apple Inc. (AAPL) Stock Analysis:

    Current Market Data:
    - Stock Price: $252.29
    - Daily Change: +$4.84 (+1.96%)
    - Volume: 45.2M shares
    - Market Cap: $3.74T

    Company Overview:
    Apple Inc. is a multinational technology company that designs, manufactures,
    and markets consumer electronics, computer software, and online services.
    Hardware products include iPhone, iPad, Mac, Apple Watch, and Apple TV.

    Recent News:
    1. Apple reports strong Q4 earnings with iPhone sales up 15% YoY
    2. New AI features announced for upcoming iOS update
    3. Partnership with major automotive manufacturer for CarPlay expansion

    Industry Position:
    Technology sector, Consumer Electronics
    Exchange: NASDAQ NMS - GLOBAL MARKET
    """

    print("📊 Using prebuilt Apple data example...")
    analysis = analyze_investment_data(market_data, args.symbol)
    display_analysis("APPLE INC. ANALYSIS", analysis, args.symbol)

    # ============================================================================
    # INPUT METHOD 2: SIMPLE EXAMPLE_FINNHUB_API_CONNECTION.PY OUTPUT USAGE (UNCOMMENT TO USE)
    # ============================================================================

    # 📊 Option: Use example_finnhub_api_connection.py output (uncomment below to enable)

    # market_data_from_example = get_data_from_example_py() #method runs example_finnhub_api_connection.py and captures all its output
    # analysis = analyze_investment_data(market_data_from_example, args.symbol)
    # display_analysis("EXAMPLE_FINNHUB_API_CONNECTION.PY OUTPUT ANALYSIS", analysis, args.symbol)


    # ============================================================================
    # INPUT METHOD 3: USE DATA FROM FILE (COMMENTED OUT)
    # ============================================================================

    
    # Uncomment this section to use data from a file

    # def get_data_from_file(file_path):
    #     try:
    #         with open(file_path, 'r') as file:
    #             return file.read()
    #     except FileNotFoundError:
    #         return f"❌ File not found: {file_path}"
    #     except Exception as e:
    #         return f"❌ Error reading file: {e}"

    # Use this instead of the prebuilt string:
    # file_path = "path/to/your/market_data.txt"  # Change this to your file path
    # market_data = get_data_from_file(file_path)
    # analysis = analyze_investment_data(market_data, args.symbol)
    # display_analysis("FILE-BASED ANALYSIS", analysis, args.symbol)
    

    print("\n✅ Analysis complete!")

if __name__ == '__main__':
    main()
