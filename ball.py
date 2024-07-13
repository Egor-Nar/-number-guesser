from random import*
import time
answers =["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
time.sleep(0.2)
print('Привет,', name)
time.sleep(0.5)

def answ(answers):
    stop_ = ['...','Одну секунду...','Еще минутку...','Тяжело...','Я почти закончил...','Я обязательно найду ответ...']
    F = True
    while F != False:
        question = input('Что ты хочешь узнать?')
        for i in range(randint(1,5)):
            time.sleep(0.7)
            print(stop_[randint(1,len(stop_)-1)])
            time.sleep(1)
            print("...")
        print(answers[randint(1,len(answers)-1)])

        Y_N = input('Хочешь узнать что-то еще?')
        while Y_N.lower() != 'no' and Y_N.lower() != 'нет' and Y_N.lower() != 'yes'and Y_N.lower() != 'да':
            print("Я тебя не понимаю")
            Y_N = input('Хочешь узнать что-то еще? Да или Нет?')
        if Y_N.lower() == 'no' or Y_N.lower() == 'нет':
            F = False
            break
        elif  Y_N.lower() == 'yes' or Y_N.lower() == 'да':
            answ(answers)
    return time.sleep(0.5), print("Надеюсь я отвветил на все твои вопросы")
answ(answers)
time.sleep(0.5)
print("Уходи и больщше не возвращайся")
time.sleep(1.2)







