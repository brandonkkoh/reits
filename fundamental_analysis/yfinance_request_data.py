import yfinance as yf
import pandas as pd
import os

# List of stock codes
# stock_codes = [
#     'C38U.SI', 'N2IU.SI', 'BUOU.SI', 'C2PU.SI', 'AW9U.SI', 'HMN.SI', 'Q5T.SI', 'J85.SI', 
#     'A17U.SI', 'M44U.SI', 'ME8U.SI', 'K71U.SI', 'MXNU.SI', 'OXMU.SI', 'J69U.SI', 'SK6U.SI', 
#     'P40U.SI', 'AJBU.SI', 'DCRU.SI'
# ]

data_extracted = [
    {"Name": "AIMS APAC REIT", "Stock Code": "O5RU", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 1014},
    {"Name": "ARA US Hospitality Trust", "Stock Code": "XZL", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 220},
    {"Name": "BHG Retail REIT", "Stock Code": "BMGU", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 255},
    {"Name": "CapitaLand Ascendas REIT", "Stock Code": "A17U", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 11256},
    {"Name": "CapitaLand Ascott Trust", "Stock Code": "HMN", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 3313},
    {"Name": "CapitaLand China Trust", "Stock Code": "AU8U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 1142},
    {"Name": "CapitaLand India Trust", "Stock Code": "CY6U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 1313},
    {"Name": "CapitaLand Integrated Commercial Trust", "Stock Code": "C38U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 13334},
    {"Name": "CDL Hospitality Trusts", "Stock Code": "J85", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 1191},
    # {"Name": "Cromwell European REIT", "Stock Code": "CWBU", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 1144},
    {"Name": "Daiwa House Logistics Trust", "Stock Code": "DHLU", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 397},
    {"Name": "Dasin Retail Trust", "Stock Code": "CEDU", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 19},
    {"Name": "Digital Core REIT", "Stock Code": "DCRU", "Property Sub-segment": "Specialized", "Market Cap (S$Mil)": 1008},
    {"Name": "EC World REIT", "Stock Code": "BWCU", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 227},
    {"Name": "Elite Commercial REIT", "Stock Code": "MXNU", "Property Sub-segment": "Office", "Market Cap (S$Mil)": 241},
    {"Name": "ESR-LOGOS REIT", "Stock Code": "J91U", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 2075},
    {"Name": "Far East Hospitality Trust", "Stock Code": "Q5T", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 1247},
    {"Name": "First REIT", "Stock Code": "AW9U", "Property Sub-segment": "Health Care", "Market Cap (S$Mil)": 511},
    {"Name": "Frasers Centrepoint Trust", "Stock Code": "J69U", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 3855},
    {"Name": "Frasers Hospitality Trust", "Stock Code": "ACV", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 799},
    {"Name": "Frasers Logistics & Commercial Trust", "Stock Code": "BUOU", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 3570},
    {"Name": "IREIT Global", "Stock Code": "UD1U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 377},
    {"Name": "Keppel DC REIT", "Stock Code": "AJBU", "Property Sub-segment": "Specialized", "Market Cap (S$Mil)": 3102},
    {"Name": "Keppel Pacific Oak US REIT", "Stock Code": "CMOU", "Property Sub-segment": "Office", "Market Cap (S$Mil)": 190},
    {"Name": "Keppel REIT", "Stock Code": "K71U", "Property Sub-segment": "Office", "Market Cap (S$Mil)": 3188},
    {"Name": "Lendlease Global Commercial REIT", "Stock Code": "JYEU", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 1331},
    {"Name": "Lippo Malls Indonesia Retail Trust", "Stock Code": "D5IU", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 108},
    {"Name": "Manulife US REIT", "Stock Code": "BTOU", "Property Sub-segment": "Office", "Market Cap (S$Mil)": 154},
    {"Name": "Mapletree Pan Asia Commercial Trust", "Stock Code": "N2IU", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 6414},
    {"Name": "Mapletree Industrial Trust", "Stock Code": "ME8U", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 5983},
    {"Name": "Mapletree Logistics Trust", "Stock Code": "M44U", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 6471},
    {"Name": "OUE REIT", "Stock Code": "TS0U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 1428},
    # {"Name": "Paragon REIT", "Stock Code": "SK6U", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 2430},
    {"Name": "Parkway Life REIT", "Stock Code": "C2PU", "Property Sub-segment": "Health Care", "Market Cap (S$Mil)": 2118},
    {"Name": "Prime US REIT", "Stock Code": "OXMU", "Property Sub-segment": "Office", "Market Cap (S$Mil)": 208},
    {"Name": "Sabana Industrial REIT", "Stock Code": "M1GU", "Property Sub-segment": "Industrial", "Market Cap (S$Mil)": 371},
    {"Name": "Sasseur REIT", "Stock Code": "CRPU", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 841},
    {"Name": "Starhill Global REIT", "Stock Code": "P40U", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 1098},
    {"Name": "Suntec REIT", "Stock Code": "T82U", "Property Sub-segment": "Diversified", "Market Cap (S$Mil)": 3059},
    {"Name": "United Hampshire US REIT", "Stock Code": "ODBU", "Property Sub-segment": "Retail", "Market Cap (S$Mil)": 312},
]

# data_extracted = [
#     {"Name": "CapitaLand Ascott Trust", "Stock Code": "HMN", "Property Sub-segment": "Hospitality", "Market Cap (S$Mil)": 3313},
# ]

# List of stock codes (39 companies)
# Extract stock codes from the data_extracted list and append ".SI" to each
stock_codes = [f'{stock["Stock Code"]}.SI' for stock in data_extracted]

# Display the corrected stock codes
stock_codes

# Create a folder to store the data
folder_name = "company_data"
os.makedirs(folder_name, exist_ok=True)

# Loop through each stock and extract data
for stock in stock_codes:
    print(f"Fetching data for {stock}...")

    try:
        # Get stock data
        ticker = yf.Ticker(stock)

        # === 1. FINANCIAL STATEMENTS ===
        income_statement = ticker.financials
        balance_sheet = ticker.balance_sheet
        cash_flow = ticker.cashflow

        # === 2. COMPANY PROFILE INFO ===
        company_info = pd.DataFrame([ticker.info])  # Convert dict to DataFrame

        # === 3. DIVIDENDS ===
        dividends = ticker.dividends.reset_index()

        # === 4. ANALYST RECOMMENDATIONS ===
        recommendations = ticker.recommendations.reset_index() if ticker.recommendations is not None else None

        # === 5. STOCK PRICE HISTORY (LAST 5 YEARS) ===
        stock_price_history = ticker.history(period="5y").reset_index()

        # Save data to CSV files
        income_statement.to_csv(os.path.join(folder_name, f"{stock}_income_statement.csv"))
        balance_sheet.to_csv(os.path.join(folder_name, f"{stock}_balance_sheet.csv"))
        cash_flow.to_csv(os.path.join(folder_name, f"{stock}_cash_flow.csv"))
        company_info.to_csv(os.path.join(folder_name, f"{stock}_company_info.csv"), index=False)
        dividends.to_csv(os.path.join(folder_name, f"{stock}_dividends.csv"), index=False)
        if recommendations is not None:
            recommendations.to_csv(os.path.join(folder_name, f"{stock}_recommendations.csv"), index=False)
        stock_price_history.to_csv(os.path.join(folder_name, f"{stock}_stock_price_history.csv"), index=False)

        print(f"✅ Saved all data for {stock} in {folder_name}/")

    except Exception as e:
        print(f"❌ Error fetching data for {stock}: {e}")

print("\nAll financial data has been successfully saved in 'company_financials' folder.")
