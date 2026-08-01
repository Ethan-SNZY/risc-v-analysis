import sqlite3 #In Progress
import pandas as pd
from datetime import date

#Create database holdings

conn = sqlite3.connect('data/riscv_pulse.db')
cursor = conn.cursor()
print('Connected to database')

#Create Tables - Re-runnable
cursor.execute('''
CREATE TABLE IF NOT EXISTS github_metrics (
    date TEXT,
    repo TEXT,
    stars INTEGER,
    recent_commits INTEGER
    )
    ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS trends_metrics (
    date TEXT,
    riscv_interest TEXT,
    arm_interest INTEGER,
    x86_interest INTEGER
    )
    ''')

conn.commit()
print('Tables created successfully')

#load data from csv files into git_hub metrics
github_df = pd.read_csv('data/stars_and_commits.csv')
github_df["date"]= str(date.today())

github_df.to_sql("github_metrics", conn, if_exists="append", index=False)
print(f'Loaded {len(github_df)} rows into github_metrics')