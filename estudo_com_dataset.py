import sqlite3
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

DATA_URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
OUT_DB = "airline_data.db"
OUT_PLOT = "grafico.png"

def download_and_load(url: str) -> pd.DataFrame:
    print("======================================")
    print(f"Log : [{datetime.now()}]")
    print(f"Baixando dados de: {url}")
    print("======================================")
    df = pd.read_csv(url, parse_dates=["Month"])
    print("Dataset foi carregado com sucesso!")
    print(f"Linhas: {len(df)}, Colunas: {df.shape[1]}")
    print("======================================")
    return df

def quick_inspect(df: pd.DataFrame):
    print("\n---------- HEAD ----------")
    print(df.head())
    print("======================================")
    print("\n---------- INFO ----------")
    print(df.info())
    print("======================================")
    print("\n------ Estatísticas descritivas ------")
    print(df.describe())

def plot_passenger_trend(df: pd.DataFrame, out_file: str):
    plt.figure(figsize=(10,6))
    plt.plot(df["Month"], df["Passengers"], marker="o")
    plt.title("Número de passageiros ao longo do tempo")
    plt.xlabel("Datas")
    plt.ylabel("Passageiros")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_file)
    plt.close()
    print("\n======================================")
    print(f"\nGráfico salvo como : {out_file}")

def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"\nTabela : {table_name} - Salva em : {db_path}")

def main():
    df = download_and_load(DATA_URL)
    quick_inspect(df)
    plot_passenger_trend(df, OUT_PLOT)
    save_to_sqlite(df, OUT_DB, "airline_passengers")

    print("\n======================================")
    print("✅ Pipeline concluído com sucesso!")
    print("======================================")
    print("\n")

if __name__ == "__main__":
    main()
