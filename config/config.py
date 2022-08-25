import os

import yaml
from jinja2 import Environment, FileSystemLoader


class Config:

    db_postgresql_uri: str
    __env: Environment

    @classmethod
    def load_config(cls):
        cls.__set_jinja_env()
        config = cls.__env.get_template('config.yaml').render()
        loaded = yaml.safe_load(config)
        cls.__set_db_postgresql_uri(**loaded['db']['postgresql'])

    @classmethod
    def __set_db_postgresql_uri(cls, **db_params):
        if not type(db_params['port']) is int:
            raise TypeError('parameter \'port\' must be int')

        cls.db_postgresql_uri = 'postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(**db_params)

    @classmethod
    def __set_jinja_env(cls):
        cls.__env = Environment(loader=FileSystemLoader('./config'))
        cls.__env.filters['env_override'] = lambda value, key: os.getenv(key, value)

