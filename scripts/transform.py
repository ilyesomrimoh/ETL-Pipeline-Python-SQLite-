import pandas as pd

def transform(df):
    # Fill missing Province/State with "Unknown"
    df['Province/State'] = df['Province/State'].fillna("Unknown")
    
    # Drop rows with missing critical values
    df = df.dropna(subset=['Country/Region', 'Date', 'Confirmed', 'Deaths'])
    
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Keep relevant columns
    df = df[['Province/State', 'Country/Region', 'Date', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    
    # Recalculate Active cases
    df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered'].fillna(0)
    
    print(f"Data transformed: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/covid_19_data.csv")
    df_clean = transform(df)
