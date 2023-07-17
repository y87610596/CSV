import sys
import csv

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:]

with open(src, "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

for change in changes:
    column, row, value = change.split(',')
    column = int(column)
    row = int(row)
    rows[row][column] = value

for row in rows:
    result =','.join(row)
    print(result)

with open(dst, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
