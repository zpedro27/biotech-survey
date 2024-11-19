import requests
import pandas as pd
import io



def load_data(year, cfg: dict):
    
    year = str(year)

    url = f"https://docs.google.com/spreadsheets/d/{cfg['DOCID']}/export?format=csv&gid={cfg['GID'][year]}"

    data = requests.get(url).content

    bytes_io = io.BytesIO(data)

    return pd.read_csv(bytes_io)


def value_replacement(df: pd.DataFrame, replacement: dict, column: str):
    for old, new in replacement.items():
        df[column] = df[column].str.replace(old, new)
    return df
