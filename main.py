import os

from sqlalchemy import create_engine

from config.config import Config
from tasks.air_quality_etl import AirQualityEtl
from tasks.air_quality_parameters_etl import AirQualityParametersEtl
from tasks.air_quality_stations_etl import AirQualityStationsEtl

if __name__ == '__main__':
    Config.load_config()
    engine = create_engine(Config.db_postgresql_uri, echo=True)

    AirQualityEtl(engine, 'data/air_quality_long.csv').start()
    AirQualityParametersEtl(engine, 'data/air_quality_parameters.csv').start()
    AirQualityStationsEtl(engine, 'data/air_quality_stations.csv').start()
