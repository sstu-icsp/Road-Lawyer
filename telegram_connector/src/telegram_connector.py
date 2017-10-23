import requests
import const
import json

URL = "https://api.telegram.org/bot" + const.token


def get_updates_json():  
    # ��������� ����������
    response = requests.get(URL + '/getUpdates')
    return response.json()


def get_userdata():  
    # ��������� �� ������������ � ������ ��������
    userdata = get_updates_json()
    user_id = userdata['result'][-1]['message']['from']['id']
    user_text = userdata['result'][-1]['message']['text']
    data = {'user_id': user_id, 'user_text': user_text}
    file = open('updates.txt', 'a')
    file.write('id = ' + str(data['user_id']) + '\n\ttext = ' + str(data['user_text']) + '\n')
    file.close()
    return data


def send_message(chat_id, text):  
    # �������� ���������
    url = URL + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + text
    requests.get(url)
