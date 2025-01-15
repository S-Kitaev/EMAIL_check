import imaplib
import time
import re
import serial


# Инициализация параметров
mail_pass = "{пароль для внешних приложений}"
username = "{почта}"
port = 'COM{номер USB порта}'


def checker():
    imap_server = "imap.mail.ru"
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(username, mail_pass)
        ser = serial.Serial(port, 9600)
        none = "none"

        # Инициализация счётчика
        match = re.search(r'\d+', str(imap.select("INBOX")[1]))
        changer = int(match.group())

        # Работа считывателя пришедшего письма
        start = time.time()

        while time.time() - start < 30:
            time.sleep(1)  # Увеличен интервал проверки
            try:
                match = re.search(r'\d+', str(imap.select("INBOX")[1]))
                x = int(match.group())
                if x > changer:
                    print('Пришло новое письмо!')
                    time.sleep(1)
                    ser.write("sign".encode())
                    time.sleep(1)

                    changer = x
                else:
                    time.sleep(1)
                    ser.write(none.encode())
                    time.sleep(1)

            except imaplib.IMAP4.abort:
                print("Соединение с сервером потеряно, повторное подключение...")
                break

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        try:
            imap.logout()
            ser.close()
        except:
            pass


while True:
    checker()