import pandas as pd
from content_search import user_list, questions_dict, answer_list, number_of_questions
from create_answer import result_lists, correct_answer_list

table = {}
questions_list = []


for i in range(1, number_of_questions+1, 1):
    questions_list.append(questions_dict[i])

print(questions_list)

table['Вопросы'] = questions_list
table['Правильные ответы'] = correct_answer_list

ind = 0
for user in user_list:
    for q in range(1, 3, 1):
        if q == 1:
            table[f'{user}'] = answer_list[ind]
        else:
            table[f'Результат проверки пользователя:{user}'] = result_lists[ind]
    ind += 1

df = pd.DataFrame(table)

df.to_excel('./test2.xlsx', sheet_name='Название листа', index=False)
