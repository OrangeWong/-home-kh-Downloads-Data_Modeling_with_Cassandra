import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster

from sql_queries import *


NEW_EVENT_DATAFILE = './event_datafile_new.csv'


def load_event_datafile():
    """ Read and load the event data files.
    
    Returns:
        full_data_rows_list (list): A list containing the event data.
    
    """
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

    # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
    
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    num_files = len(file_path_list)
    
    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

     # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line)
    print("{} data files are loaded.\n".format(num_files))
    return full_data_rows_list


def write_event_data(data_list):
    """Creating a smaller event data csv file called event_datafile_new csv 
       that will be used to insert data into the Apache Cassandra tables 
    
    Parameters:
        data_list (list): A list of lines, each line contain a record of event data.
    Returns:
        None
    """
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open(NEW_EVENT_DATAFILE, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender',
                         'itemInSession','lastName','length',
                         'level','location','sessionId','song','userId'])
        
        ignored_records_num = 0
        for row in data_list:
            if (row[0] == ''):
                ignored_records_num += 1
                continue
            writer.writerow((row[0], row[2], row[3], row[4], 
                             row[5], row[6], row[7], row[8], 
                             row[12], row[13], row[16]))  
        print(
            "{} records are igonred because of the empty artist.\n".format(
                ignored_records_num
            )
        )

            
def read_event_data():
    """Read the event data into a list.
    
    Returns:
        line (generator): a generator that contains the event data.
    """
    with open(NEW_EVENT_DATAFILE, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            formats = [str, str, str, int, str, float, str, str, int, str, int]
            line = [f(x) for x, f in zip(line, formats)]
            yield line
    

def process_data(session, drop_query, create_query, insert_query, table_name):
    """Prcess the data, then create and insert data into the table.
    
    Parameters:
        session (session): a session of the database.
        drop_query (str): a query to drop the table.
        create_query (str): a query to create the table.
        insert_query (str): a query to insert the records into the table.
        table_name (str): the name of the table.
        
    """
    session.execute(drop_query)
    session.execute(create_query)
    print("Table {} is created.\n".format(table_name))
    
    num_records = 0
    lines = read_event_data()    
    for line in lines:
        session.execute(insert_query, (x for x in line))
        num_records += 1
    print("{} records are inserted into {}.\n".format(num_records, table_name))
        
    
def main():
    # connecting to the database
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute(drop_keyspace_query)
    session.execute(create_keyspace_query)
    session.set_keyspace('project2')
    print("Connected to the database\n")
    
    # extract, and transform the event data
    data_list = load_event_datafile()
    write_event_data(data_list)
    
    # to create, and insert data into database
    for drop_q, create_q, insert_q, table_name in zip(drop_table_queries, create_table_queries, insert_table_queries, table_names):
        process_data(session, drop_q, create_q, insert_q, table_name)
            
            
if __name__ == "__main__":
    main()
    
    


