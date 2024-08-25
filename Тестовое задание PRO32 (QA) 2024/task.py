import requests
import random
import string
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# URL
TOKEN_URL = 'https://getscreen.dev/api/openid/token' # URL для token
CHECK_URL = 'https://getscreen.dev/api/login/check' # URL для check
LOGIN_URL = 'https://getscreen.dev/api/login'  # URL для login
PROFILE_URL = 'https://getscreen.dev/api/dashboard/settings/account/update'  # URL для update

# Функция генерации случайной строки
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

username = 'bukharinav94@gmail.com'  # Логин
password = 'n9D7XgEKPA'  # Пароль

# 1:Вход в ЛК
session = requests.Session()

login_check = {
    'login': username,
}
login_data = {
    'login': username,
    'password': password,
}

response = session.get(TOKEN_URL, headers={ 'x-requested-with': 'XMLHttpRequest' })
logging.info(f"Login Response: {response.status_code} - {response.text}")

response = session.post(CHECK_URL, json=login_check, headers={ 'x-requested-with': 'XMLHttpRequest' })
logging.info(f"Login Response: {response.status_code} - {response.text}")

response = session.post(LOGIN_URL, json=login_data, headers={ 'x-requested-with': 'XMLHttpRequest' })
logging.info(f"Login Response: {response.status_code} - {response.text}")
#####print(session.cookies.get_dict())

if response.status_code == 200:
    logging.info('Login Succeed')
else:
    logging.error('Login Failed')
    exit()

# 2: Сохранение аутентификационной cookie llt
cookies = session.cookies.get_dict()
logging.info(f"Cookies: {cookies}")



# 3: Изменение полей "Имя" и "Фамилия"
new_first_name = random_string()
new_last_name = random_string()

update_data = {
    "ad_allowed": "false",
    "beta": "true",
    "country": "ru",
    "dateformat": "0",
    "language": "en",
    "name": new_first_name,
    "surname": new_last_name,
    "timezone": "0"
}

response = session.put(PROFILE_URL, json=update_data, headers={ 'x-requested-with': 'XMLHttpRequest' })
logging.info(f"Update Profile Response: {response.status_code} - {response.text}")

if response.status_code == 200:
    logging.info("Profile Update Succeed")
else:
    logging.error("Profile Update Failed")



# 4: Проверка изменений
response = session.get(PROFILE_URL)
logging.info(f"Get Profile Response: {response.status_code} - {response.text}")

if response.status_code == 200:
    user_data = response.json()
    if user_data['name'] == new_first_name and user_data['surname'] == new_last_name:
        logging.info("Profile Data Verification Succeed")
    else:
        logging.error("Profile Data Verification Failed")
else:
    logging.error("Failed to Get Profile Data")