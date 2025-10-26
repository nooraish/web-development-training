import xlsxwriter

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('expenses.xlsx')
worksheet = workbook.add_worksheet()

# Data to write
expenses = [
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50]
]

# Write data row by row (rows and columns are zero-indexed)
row = 0
col = 0

worksheet.write(row, col, 'item') # first column heading
worksheet.write(row, col + 1, 'cost') # second column heading
row += 1

for item, cost in expenses:
    worksheet.write(row, col, item)      # Write item name
    worksheet.write(row, col + 1, cost)  # Write cost
    row += 1

# Add a formula to calculate total
worksheet.write(row, col, 'Total')
worksheet.write_formula(row, col + 1, '=SUM(B2:B5)')

# Close the workbook (important!)
workbook.close()

print("Excel file created successfully!")