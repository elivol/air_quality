import pandas as pd

from tasks.base_etl_from_csv import BaseEtlFromCSV


class AirQualityStationsEtl(BaseEtlFromCSV):

    def extract(self) -> pd.DataFrame:
        df = pd.read_csv(self.source)
        return df

    def load(self, df: pd.DataFrame):
        df.to_sql("air_quality_stations", self.engine, index=False, chunksize=1000, if_exists='replace')
