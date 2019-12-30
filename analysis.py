import sqlite3
import json
from datetime import datetime
from pyexcel_ods import get_data, save_data

def create_db_connection():
  return sqlite3.connect(':memory:')

def fill_transactions(db, ods_file):
  c = db.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS transactions (year INTEGER, month INTEGER, day INTEGER, vendor TEXT, credit REAL, debit REAL, account TEXT, category TEXT)')

  transactionData = get_data(ods_file)

  for _, sheet in transactionData.items():
    for row in sheet[1:]:
      if len(row) == 0:
        continue

      d = datetime.strptime(row[0], '%Y-%m-%d')
      c.execute('INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (d.year, d.month, d.day, row[1], row[2], row[3], row[4], row[5]))

  db.commit()

def fill_taxonomy(db, json_file):
  c = db.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS full_taxonomy (id TEXT, parent TEXT, name TEXT, spend INTEGER)')
  c.execute('CREATE VIEW IF NOT EXISTS taxonomy AS SELECT * FROM full_taxonomy WHERE spend = 1')
  with open(json_file) as json_file:
    data = json.load(json_file)

    for key, value in data.items():
      c.execute('INSERT INTO full_taxonomy VALUES (?, ?, ?, ?, ?)',
        (key,
        value.get('parent', None),
        value.get('name'),
        1 if value.get('spend', True) else 0))
  
  db.commit()
