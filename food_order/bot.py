import telebot
from telebot import types
import requests

# Замените на токен вашего бота
bot = telebot.TeleBot('5859062410:AAG3dwVmfjCFk1loJSAD1cVpMsZnkprCBU8')

# Замените на URL вашего API
API_URL = 'http://127.0.0.1:8000/'

# Словарь для хранения заказов пользователей
orders = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Что вы хотите сделать?")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    response = requests.get(API_URL + 'menuitems/')
    menu_items = response.json()
    for item in menu_items:
        bot.send_message(message.chat.id, f"{item['product']['name']} - {item['product']['price']}")
    bot.send_message(message.chat.id, "Чтобы добавить продукт в заказ, отправьте /add и номер продукта, например: /add 1")

@bot.message_handler(commands=['add'])
def add_to_order(message):
    product_id = message.text.split()[1]
    if message.chat.id not in orders:
        orders[message.chat.id] = []
    orders[message.chat.id].append(product_id)
    bot.send_message(message.chat.id, f"Продукт {product_id} добавлен в ваш заказ")

@bot.message_handler(commands=['order'])
def send_order(message):
    if message.chat.id not in orders or not orders[message.chat.id]:
        bot.send_message(message.chat.id, "Ваш заказ пуст")
        return

    order_data = {
        'user': message.chat.id,
        'menu_items': orders[message.chat.id]
    }
    response = requests.post(API_URL + 'orders/', data=order_data)
    order = response.json()
    bot.send_message(message.chat.id, f"Ваш заказ оформлен. Номер заказа: {order['id']}. Сумма к оплате: {order['total_price']}")

# Добавьте обработчики для других команд и сообщений

bot.polling()
