from peewee_async import PooledPostgresqlDatabase
from config import *

PostgresDB = PooledPostgresqlDatabase(PG_DATABASE, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)