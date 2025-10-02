from extract import extract
from transform import transform
from load import load

def run_pipeline():
    file_path = "data/covid_19_data.csv"
    df = extract(file_path)
    df_clean = transform(df)
    load(df_clean)

if __name__ == "__main__":
    run_pipeline()
