from content_search import answer_list
from openai import OpenAI
import os
from creating_txt_from_pdf import pdf_list
from recording_cor_ans import correct_answer_list
os.environ["OPENAI_API_KEY"] = "токен для подключения к API OPENAI GPT"


client = OpenAI()

result_lists = []
result_list = []

x = 1
for ind_anc in range(len(pdf_list)):
    for correct_answer in correct_answer_list:
        ind_quan = correct_answer_list.index(correct_answer)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f'есть ключевые тезисы:"{correct_answer}" есть ли они в тексте: "{answer_list[ind_anc-1][ind_quan]}".В ответе отметь присутствующие тезисы словами да или нет и выведи число обнаруженых тезисов к общему количеству' }
            ]
        )
        с = completion.choices[0].message
        result_list.append(с.content)
        print(f'Правильный ответ-{correct_answer}\nОтвет пользователя -{answer_list[ind_anc-1][ind_quan]}\nпроверка-{с.content}')
        print(f"Вопрос: {ind_quan} анкеты номер: {x} обработан")
        x += 1
        ind_quan = ind_quan + 1
    result_lists.append(result_list)
print('Проверка завершена!')
