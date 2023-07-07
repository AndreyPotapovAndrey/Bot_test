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

                usr = vk_api.users.get(user_ids=usr_id,
                                       fields="city, sex, bdate", v=5.89)
                print(usr)



