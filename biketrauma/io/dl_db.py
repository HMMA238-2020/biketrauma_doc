from download import download
import pandas as pd

from biketrauma.io import url_db, path_target


def dl_db(url=url_db, target_name=path_target):
  download(url, target_name, replace=False)

def load_db():
  dl_db()
  df_bikes = pd.read_csv("bicycle_db.csv", na_values="", low_memory=False, converters={'data': str, 'heure': str})
  return df_bikes
