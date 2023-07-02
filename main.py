import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from decouple import config

group_token = config('group_token', default='')

group_id = '221375984'


def main():
    vk_session = vk_api.VkApi(token=group_token)
    session_api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id)

    for event in longpoll.listen():
        ct = event.messege.text.lower()
        content = ct.split(" ")
        user_id = event.message.from_id
        peer_id = event.message.peer_id
        user_name_first = session_api.users.get(user_ids=(user_id))[0]['first_name']
        user_name_last = session_api.users.get(user_ids=(user_id))[0]['last_name']
        print(f'Кто написал: {user_name_first}{user_name_last}\nЧто написал: {ct}')

        if content[0][0] == '/':
            if content[0][1:] == 'ping':
                session_api.messeges.send(peer_id=peer_id, massage='pong!', random_id=0)
            if content[0][1:] == 'ping':
                session_api.messeges.send(peer_id=peer_id, massage='ping!', random_id=0)


if __name__ == '__main__':
    main()



