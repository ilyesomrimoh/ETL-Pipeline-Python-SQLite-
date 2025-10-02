import sqlite3

def load(df, db_path="database/covid19.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql('covid19', conn, if_exists='replace', index=False)
    conn.commit()
    
    print("Data loaded into database successfully.")
    
    cur = conn.cursor()
    
    # Total rows
    cur.execute("SELECT COUNT(*) FROM covid19")
    print(f"Total rows in DB: {cur.fetchone()[0]}")
    
    # Top 5 countries by confirmed cases
    cur.execute("""
        SELECT [Country/Region], SUM(Confirmed) as TotalConfirmed 
        FROM covid19 
        GROUP BY [Country/Region] 
        ORDER BY TotalConfirmed DESC 
        LIMIT 5
    """)
    print("Top 5 countries by confirmed cases:")
    for row in cur.fetchall():
        print(row)
    
    conn.close()

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    
    df = extract("../data/covid_19_data.csv")
    df_clean = transform(df)
    load(df_clean)
