import MySQLdb
from pandas import read_sql
import warnings
import hashlib
from sqlalchemy import create_engine
from abc import ABC, abstractmethod
import cx_Oracle
import psycopg2
import sqlite3
import pymssql

class DBconn(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def __del__(self)->None:
        try:
            self._conn.close()
        except:
            pass
    @property
    @abstractmethod
    def URL(self):
        pass

    def to_DataFrame(self,cmd:str):
        if not (cmd.lower().startswith('select') or cmd.lower().startswith('show')):
            raise ValueError("to_DataFrame does only supports 'select' or 'show' commands.")
        return read_sql(cmd,self._conn)

    def execute(self,cmd:str):
        if cmd.lower().startswith('select'):
            raise ValueError("execute does not support 'select' operations. Use 'to_DataFrame' method for queries.")
        if cmd.lower().startswith('show'):
            raise ValueError("execute does not support 'show' operations. Use 'to_DataFrame' method for queries.")
        try:
            cur=self._conn.cursor()
            cur.execute(cmd)
            self._conn.commit()
        except Exception as e:
            warnings.warn(str(e))

    def to_csv(self, cmd:str, file_name:str,encoding:str="utf-8"):
        try:
            self.to_DataFrame(cmd).to_csv(file_name+".csv", index=False,encoding=encoding)
        except Exception as e:
            warnings.warn(str(e))

    def to_excel(self, cmd:str, file_name:str):
        try:
            self.to_DataFrame(cmd).to_excel(file_name+".xlsx", index=False)
        except Exception as e:
            warnings.warn(str(e))

    def to_tsv(self, cmd:str, file_name:str,encoding:str="utf-8"):
        try:
            self.to_DataFrame(cmd).to_csv(file_name+".tsv", sep="\t",index=False,encoding=encoding)
        except Exception as e:
            warnings.warn(str(e))
    def to_sql(self,cmd:str,name:str,other):
        if not (cmd.lower().startswith('select') or cmd.lower().startswith('show')):
            raise ValueError("to_sql does only supports 'select' or 'show' commands.")
        try:
            with create_engine(other.URL).connect() as conn:
                self.to_DataFrame(cmd).to_sql(name,conn,index=False,if_exists="replace")
        except Exception as e:
            warnings.warn(str(e))
class MYSQLConn(DBconn):
    def __init__(self,host:str='127.0.0.1',user:str="root",password:str=None,database:str="mysql",port:str|int=3306) -> None:
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=MySQLdb.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
    @property
    def URL(self):
        return f'mysql+mysqldb://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'
class MSSQLConn(DBconn):
    def __init__(self,host:str='127.0.0.1',user:str="sa",password:str=None,database:str="master",port:str|int=1433) -> None:
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=pymssql.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
    @property
    def URL(self):
        return f'mssql+pyodbc://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'
class PostgresqlConn(DBconn):
    def __init__(self,host:str='127.0.0.1',user:str="postgres",password:str=None,database:str="postgres",port:str|int=5432) -> None:
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=psycopg2.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
    @property
    def URL(self):
        return f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'
class OracleConn(DBconn):
    def __init__(self,host:str='127.0.0.1',user:str="system",password:str=None,database:str="xe",port:str|int=1521) -> None:
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=cx_Oracle.connect(self.__user,self.__password,f'{self.__host}:{self.__port}/{self.__database}')
    @property
    def URL(self):
        return f'oracle+cx_oracle://{self.__user}:{self.__password}@{self.__host}:{self.__port}/?service_name={self.__database}'
class SQLite(DBconn):
    def __init__(self,file_path:str) -> None:
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        self.__file_path=file_path
        self._conn=sqlite3.connect(file_path)
    @property
    def URL(self):
        return f'sqlite://{self.__file_path}'

def multi_hash(text)->str:
    text = str(text)
    for i in range(0, ord(text[-1]) % 10):
        if i &1 == 1:
            text = hashlib.sha256(text.encode()).hexdigest()
        else:
            text = hashlib.sha512(text.encode()).hexdigest()
    return text
