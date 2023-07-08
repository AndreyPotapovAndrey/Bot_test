import time
import datetime
import vk_api
import vk
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import datetime
import re
import base
from decouple import config
import requests
from pprint import pprint

group_token = config('group_token', default='')

vk1 = vk_api.VkApi(token=group_token)


def write_msg(rand_int, user_id, message):
    vk1.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': rand_int})


# слушаем пул в ВК
longpoll = VkLongPoll(vk1)
day_time = datetime.datetime.now()
day_time = day_time.strftime('%Y-%m-%d %H:%M:%S')
msg = (day_time + ' ' + 'Дрон к вашим услугам!')
print(msg)

# Цикл, который слушает, не пришло ли сообщение
while True:
    time.sleep(5)
    for event in longpoll.listen():

        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            if event.to_me:
                request = event.text
                randint = random.randint(100000000, 900000000)
                request = request.lower()
                chat_id = vk1.method('messages.getConversations')
                # pprint(chat_id)
                chat_id = chat_id['items']
                # pprint(chat_id[0]['last_message']['from_id'])

                usr_id = chat_id[0]['last_message']['from_id']  # извлекаем id пользователя
                # print(usr_id)
                txt_usr = request  # текст, который ввёл пользователь
                time_msg = chat_id[0]['last_message']['date']  # извлекаем время сообщения
                # print(txt_usr)

                """Приводим дату в нормальный вид"""
                value = datetime.datetime.fromtimestamp(time_msg)
                time_message = (value.strftime('%Y-%m-%d %H:%M:%S'))
                # print(time_message, end=" ")
                # print(txt_usr)

                api = vk.API(access_token=group_token)
                user = api.users.get(user_ids=usr_id,
                                    fields="city, sex, bdate", v=5.89)
                # print(usr)


                first_name = (user[0]['first_name'])
                last_name = (user[0]['last_name'])
                fn = (user[0]['first_name'] + ' ' + user[0]['last_name'])
                # print(fn)

                # Если город не указан или скрыт, то напишем: где вы живете?
                try:
                    city = (user[0]['city']['title'])
                except KeyError:
                    city = 'В каком городе вы живёте?'
                # print(city)
                print(time_message, '[', fn, ']', ':', txt_usr)

                # Произвольный ответ на то, что написали Дрону, из массива со словами
                rnd_privet = random.choice(base.privet)
                rnd_poka = random.choice(base.poka)
                rnd_blag = random.choice(base.blag)
                rnd_spasib = random.choice(base.spasib)

                # Время ответа бота
                day_time = datetime.datetime.now()
                day_time = day_time.strftime('%Y-%m-%d %H:%M:%S')

                # Прверка слов приветствия в полученном сообщении + отправка приветствия
                for pattern in base.privet:
                    # print('Поиск "%s" в "%s" ->' % (pattern, request))
                    if re.search(pattern, request):
                        print(day_time + ' Ответ от бота для ' + fn + ':')
                        k = (rnd_privet.title() + ", " + fn + "! Я бот Дрон! Начнём? &#128521;! Будем искать в вашем городе?")

                        write_msg(randint, event.user_id, k)



