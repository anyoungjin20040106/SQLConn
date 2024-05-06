# SQLConn

SQLConn은 다양한 SQL 데이터베이스 관리 시스템(DBMS)에 연결하여 데이터를 쉽게 조작하고 관리할 수 있는 Python 패키지입니다. 이 패키지는 MySQL, PostgreSQL, Microsoft SQL Server, Oracle 및 SQLite 데이터베이스에 대한 지원을 포함합니다.

## 기능

- 여러 데이터베이스에 대한 통합된 인터페이스 제공
- 데이터 조회 및 조작을 위한 간편한 함수 제공
- 데이터베이스 쿼리 결과를 DataFrame으로 변환
- CSV, Excel, TSV 파일로의 데이터 출력 지원
- 다른 데이터베이스로의 데이터 이동 지원

## 지원 데이터베이스
- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle
- SQLite

## 설치 방법

파이썬과 pip가 설치된 환경에서 다음 명령어를 통해 `SQLConn` 패키지를 설치할 수 있습니다:

```bash
pip install SQLConn
```
## 사용예제
각 데이터베이스 연결 객체를 생성하고 사용하는 기본적인 방법은 다음과 같습니다:
```py
from SQLConn import MySQLConn, PostgreSQLConn

# MySQL 데이터베이스에 연결
mysql_conn = MySQLConn(host='your-host', user='your-user', password='your-password', database='your-database',port='your-port')

# MsSQL 데이터베이스에 연결
mssql_conn = MSSQLConn(host='your-host', user='your-user', password='your-password', database='your-database',port='your-port')

# PostgreSQL 데이터베이스에 연결
postgresql_conn = PostgreSQLConn(host='your-host', user='your-user', password='your-password', database='your-database',port='your-port')

# SQLite 데이터베이스에 연결
mssql_conn = SQLiteConn('your-host')

# 데이터 조회 예제
df = mysql_conn.to_DataFrame("SELECT * FROM your_table")
print(df)
```
## 로컬호스트에서 사용하기
로컬 호스트 데이터베이스 연결 객체를 생성하고 사용하는 기본적인 방법은 다음과 같습니다:
```py
from SQLConn import MySQLConn, PostgreSQLConn

# MySQL 데이터베이스에 연결
mysql_conn = MySQLConn('your-password')

# MsSQL 데이터베이스에 연결
mssql_conn = MSSQLConn('your-password')

# PostgreSQL 데이터베이스에 연결
postgresql_conn = PostgreSQLConn('your-password')

# 데이터 조회 예제
df = mysql_conn.to_DataFrame("SELECT * FROM your_table")
print(df)
```