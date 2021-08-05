from sqlalchemy import create_engine
from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from datetime import datetime
import json
import pandas as pd
import sqlite3

from .settings.db_settings import DATABASE


class Atm_dml():

    def __init__(self):
        self.db = create_engine(DATABASE['db_connection'])
        
    def fetch_newid(self):
        with self.db.begin() as conn:
            select_sql ="""SELECT max(id) as id FROM atms"""
            id=conn.execute(select_sql).fetchall()
            if  id:
                id=id[0][0]+1
            else:
                id=1     
        return id
        
    def fetch_atmdata(self):
        with self.db.begin() as conn:
            select_sql ="select * from atms order by id"
            tbl_data=conn.execute(select_sql)
            Column =conn.execute(select_sql).keys()
            data =[dict(zip(Column, row)) for row in tbl_data]
        return data
        
        
    def create_atmdata(self,record):
        with self.db.begin() as conn:
            id = self.fetch_newid()
            data=json.dumps(record)
            insert_sql=f"""
                insert into atms(id,atm_details) 
                values({id},'{data}')
                """
            conn.execute(insert_sql)

           
    def update_atmdata(self,id,record):
        with self.db.begin() as conn:
            data=json.dumps(record)
            update_sql=f"""update atms
                           set atm_details ='{data}'
                           where id={id}
                        """
            conn.execute(update_sql)
    

    def delete_atmdata(self,id):
        with self.db.begin() as conn:
            delete_sql=f"""delete from atms
                           where id={id}
                        """
            conn.execute(delete_sql)
            
    def authenticate(self,username,password):
         with self.db.begin() as conn:
            sql=f"""SELECT 1 res FROM users where username='{username}' and password='{password}'"""
            return conn.execute(sql)           
            
    def __del__(self):
        self.db.dispose()
