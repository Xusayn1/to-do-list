from core.db_settings import execute_query
import logging

logger = logging.getLogger(__name__)

done = """
    CREATE TABLE IF NOT EXISTS done ( 
    id SERIAL PRIMARY KEY,
    item VARCHAR(100) NOT NULL,
    time date NOT NULL 
    );
    """

do = """
    CREATE TABLE IF NOT EXISTS todo ( 
    id SERIAL PRIMARY KEY,
    item VARCHAR(100) NOT NULL, 
    time date NOT NULL
    ); 
"""

def create_tables() -> None:
    """
    that's for creating the tables
    :return: nothing but executes the query
    """
    execute_query(do)
    execute_query(done)
    print('Tables created successfully')
    logging.info('Tables created successfully')