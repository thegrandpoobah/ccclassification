from pyexcel_ods import get_data, save_data
from shared_funcs import format_row
import fasttext
import random
import sys

# 80% of input should be treated as training, 20% should be treated as verification
VERIFY_FACTOR = 8

transactionData = get_data(sys.argv[1])

trainFile = open("/tmp/cctransactions.train", "w")

v = []

for _, sheet in transactionData.items():
    for row in sheet[1:]:
        if len(row) < 6:
            continue

        if row[5] == '':
            continue

        v.append(format_row(row, True))

trainFile = open("/tmp/cctransactions.train", "w")

random.shuffle(v)

for row in v[:(len(v)//10)*8]:
    print(row, file=trainFile)

trainFile.close()

verifyFile = open("/tmp/cctransactions.verify", "w")

for row in v[(len(v)//10)*8:]:
    print(row, file=verifyFile)

verifyFile.close()

model = fasttext.train_supervised(
    input="/tmp/cctransactions.train", epoch=50, lr=0.8, wordNgrams=2)
print(model.test("/tmp/cctransactions.verify"))
model.save_model("cc.model")
