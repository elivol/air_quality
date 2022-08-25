import pandas as pd

from tasks.base_etl_from_csv import BaseEtlFromCSV


class AirQualityEtl(BaseEtlFromCSV):

    def extract(self) -> pd.DataFrame:
        df = pd.read_csv(self.source, parse_dates=True)
        df['date.utc'] = pd.to_datetime(df['date.utc'], utc=True)
        return df

    def load(self, df: pd.DataFrame):
        df.to_sql("air_quality", self.engine, index=False, chunksize=1000, if_exists='replace')
