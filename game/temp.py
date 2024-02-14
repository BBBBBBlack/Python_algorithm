import pandas as pd
from sqlalchemy import create_engine

# MySQL数据库连接参数
username = 'root'
password = 'Aa@123456'
hostname = 'localhost'
port = '3306'
database_name = 'your_database_name'

# 创建MySQL连接引擎
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}')

# 读取CSV文件为DataFrame
file_path = 'your_file.csv'
data = pd.read_csv(file_path)

# 将数据写入MySQL数据库中的表中，如果表不存在则会自动创建
table_name = 'your_table_name'
data.to_sql(table_name, engine, if_exists='replace', index=False)

# 关闭数据库连接
engine.dispose()