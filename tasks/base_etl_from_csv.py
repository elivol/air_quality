import pandas as pd
import sqlalchemy.engine


class BaseEtlFromCSV:

    def __init__(self, engine: sqlalchemy.engine.Engine, source: str) -> None:
        self.engine = engine
        self.source = source

    def extract(self) -> pd.DataFrame:
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

    def load(self, df: pd.DataFrame):
        pass

    def start(self):
        df = self.extract()
        df = self.transform(df)
        self.load(df)
