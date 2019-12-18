from pyexcel_ods import get_data, save_data
from shared_funcs import format_row
import fasttext
import sys

model = fasttext.load_model("cc.model")

transactionData = get_data(sys.argv[1])

for _, sheet in transactionData.items():
  for row in sheet[1:]:
    if len(row) == 0:
      continue

    p = model.predict(format_row(row, False))

    if len(row) < 6:
      row.append('')

    row[5] = p[0][0].replace('__label__', '')

save_data(sys.argv[1], transactionData)
