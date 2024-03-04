from creating_txt_from_pdf import pdf_list

number_of_questions = 30
questions_dict = {}
answer_list = []
user_list = []


for pdf in pdf_list:
    name_txt = pdf[:-4]
    str1 = open(f'ptxt/{name_txt}', encoding='windows-1251')
    s = str1.read()
    str1.close()

    # поиск пользователя
    uind1 = s.find('Пользователь: ')
    uind2 = len('Пользователь: ')
    start_user_ind = uind1 + uind2
    # print(start_user_ind)

    end_user_ind = s.find('Аттестация_ОПП')
    # print(end_user_ind)

    user = s[start_user_ind:end_user_ind]
    user_list.append(user)
    # print(user)

    # поиск вопросов и ответов

    # questions_dict = {}
    answer_list1 = []

    i = 1

    while i <= number_of_questions:
        if pdf == pdf_list[0]:
            # ищем начало вопроса
            q_str1 = str(i) + '. '
            # print(a_str1)
            q_ind1 = s.find(q_str1)
            # print(a_ind1)
            # ищем конец вопроса
            q_str2 = 'ЭссеОтвет'
            q_ind2 = s.find(q_str2)
            # print(a_ind2)
            # Получаем вопрос
            question = s[q_ind1:q_ind2]
            # print(question)
            # добавляем вопрос в словарь
            questions_dict[i] = question
            # print(questions_dict)

        # ищем начало ответа
        a_str1 = 'пользователяВарианты ответов'
        a_ind1 = s.find(a_str1) + len(a_str1)
        # ищем конец ответа
        if i == number_of_questions:
            a_str2 = 'Пользователь: '
            a_ind2 = s.find(a_str2)
        else:
            a_str2 = str(i + 1) + '. '
            a_ind2 = s.find(a_str2)
        # получаем ответ
        answer = s[a_ind1:a_ind2]
        # добавляем ответ в словарь
        answer_list1.append(answer)
        # print(answer_dict)
        # обрезаем строку и обновляем счетчик
        s = s[a_ind2:]
        i += 1
    answer_list.append(answer_list1)
