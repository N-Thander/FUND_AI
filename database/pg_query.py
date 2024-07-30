import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('DB_PASSWORD')

try:
    conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cur = conn.cursor()
    
    # User Profile Data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS UserProfileData(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email_id VARCHAR(255) NOT NULL,
            contact_number BIGINT NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    print("Table UserProfileData created successfully.")

    # User Preference
    cur.execute("""
        CREATE TABLE IF NOT EXISTS UserPreference(
            performance_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES UserProfileData(user_id),
            initial_investment INT,
            returns INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
        );              
    """)
    conn.commit()
    print("Table UserPreference created successfully")

    # User LLM Interaction
    cur.execute("""
        CREATE TABLE IF NOT EXISTS UserLLMInteraction(
            interaction_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES UserProfileData(user_id),
            question TEXT,
            prompt JSONB,
            response JSONB,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );              
    """)
    conn.commit()
    print("Table UserInteraction created successfully")

    # Company
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Company(
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR(255) NOT NULL UNIQUE
        );      
    """)
    conn.commit()
    print("Table Company created successfully")

    # Stock Market Data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS StockMarketData (
            record_id SERIAL PRIMARY KEY,
            company_id INT REFERENCES Company(company_id),
            date DATE NOT NULL,
            open_price DECIMAL(10, 2) NOT NULL,
            close_price DECIMAL(10, 2) NOT NULL,
            high_price DECIMAL(10, 2) NOT NULL,
            low_price DECIMAL(10, 2) NOT NULL,
            volume BIGINT NOT NULL,
            market VARCHAR(50) NOT NULL
        );           
    """)
    conn.commit()
    print("Table StockMarketData created successfully.")

    # Stock News Data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS StockNewsData (
            stock_news_id SERIAL PRIMARY KEY,
            stock_headline TEXT NOT NULL,
            stock_sentiment VARCHAR(10) NOT NULL,
            stock_company_id INT REFERENCES Company(company_id)
        );           
    """)
    conn.commit()
    print("Table NewsData created successfully.")

    # Mutual Funds Data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS MutualFundData(
            mfund_id SERIAL PRIMARY KEY,
            mfund_name VARCHAR(255) NOT NULL,
            ticker VARCHAR(10) NOT NULL,
            date DATE NOT NULL,
            nav DECIMAL(10, 2) NOT NULL,
            expense_ratio DECIMAL(5, 2),
            risk_level VARCHAR(10),
            fund_category VARCHAR(255)
        );        
    """)
    conn.commit()
    print("Table MutualFundData created successfully")
    
    # Gold Market Data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS GoldMarketData(
            record_id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            open_price DECIMAL(10, 2) NOT NULL,
            close_price DECIMAL(10, 2) NOT NULL,
            high_price DECIMAL(10, 2) NOT NULL,
            low_price DECIMAL(10, 2) NOT NULL,
            volume BIGINT,
            mkt_country VARCHAR(50) NOT NULL,
            mkt_state VARCHAR(50) NOT NULL,
            gold_news JSONB            
        );        
    """)
    conn.commit()
    print("Table GoldMarketData created successfully")
    

    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
