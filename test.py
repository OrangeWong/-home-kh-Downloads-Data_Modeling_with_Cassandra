import cassandra
from cassandra.cluster import Cluster

from sql_queries import *


def connect_database():
    """Connecting to the database
    
    Returns:
        session (session): a Cassandra session object
    """
    # connecting to the database
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('sparkify_event')
    return session


def main():
    session = connect_database()
    
    for select_q in select_table_queries:
        print("Runnung query: {}".format(select_q))
        rows = session.execute(select_q)
        
        print("The result from the query is:")
        for row in rows:
            print(row._asdict())
        print()
            
if __name__ == '__main__':
    main()
    