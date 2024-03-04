import gspread

gc = gspread.service_account(filename='phrasal-concord-000009-rewqerqer7f.json')

sh = gc.open("test")

worksheet = sh.worksheet("Верные ответы")

# получить список ответов из заранее созданной таблицы ответов
correct_answer_list = worksheet.col_values(2)

correct_answer_list.pop(0)
