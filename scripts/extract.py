import pandas as pd

def extract(file_path):
    df = pd.read_csv(file_path)
    print(f"Data extracted: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = extract("../data/covid_19_data.csv")
