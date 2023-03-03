import pandas

excel_data_df = pandas.read_excel('soal.xlsx')

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)