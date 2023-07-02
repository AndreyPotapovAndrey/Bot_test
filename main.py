import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from decouple import config

group_token = config('group_token', default='')

group_id = '221375984'

vk_session = vk_api.VkApi(token=group_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session, group_id)


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.message['text'].lower()
            user_dict_info = users_info(event.message['from_id'], main_process.gr_params, main_process.us_params)
            # Стартовый запрос
            if response in ['привет', 'hello', 'start', 'hi', '/', 'ghbdtn']:

                if len(user_dict_info['birth_date'].split('.')) != 3:
                    write_msg(user_dict_info['vk_id'], f"Хай, {user_dict_info['first_name']}!\n"
                                                       f" Хочешь познакомиться?\n"
                                                       f"Сколько тебе лет?"
                              )
                    # print(event.obj)
                else:
                    age = int((datetime.now() - datetime.strptime(user_dict_info['birth_date'],
                                                                  "%d.%m.%Y")).days / 365)
                    user_dict_info['age'] = age
                    write_msg(event.message['from_id'], f"Хай, {user_dict_info['first_name']}!\n"
                                                        f" Хочешь познакомиться?",
                              keyboard_creator('start'))


if __name__ == '__main__':
    main()



