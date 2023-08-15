from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup,  KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import functions as func

texts = func.get_texts()

def make_keyboard(path: dict) -> ReplyKeyboardMarkup:
    buttons = []
    for v in path.values():
        button = KeyboardButton(v)
        buttons.append(button)
    markup = ReplyKeyboardMarkup(resize_keyboard= True)

    for i in range(0, len(buttons), 2):
        try:
            markup.row(buttons[i], buttons[i+1])
        except IndexError:
            markup.row(buttons[i])

    return markup

main_keybord = make_keyboard(texts['keyboards']['main_menu'])

price_link_button = InlineKeyboardButton(texts['keyboards']['price_subscribe']['price'], url = 'https://xn–80ahhi0afh.xn–p1ai/?utm_source=telegram&utm_medium=chatbot&utm_content=tariff&utm_campaign=prodazhi_rf')
price_link_keyboard = InlineKeyboardMarkup(resize_keyboard = True).row(price_link_button)

subscribe_link_button = InlineKeyboardButton(texts['keyboards']['price_subscribe']['subscribe'], url = 'https://Продажи.рф')
subscribe_link_keyboard = InlineKeyboardMarkup(resize_keyboard = True).row(subscribe_link_button)


site_link_button = InlineKeyboardButton('🌐 На сайт', url = 'https://Продажи.рф')
channel_link_button = InlineKeyboardButton('🔔 В канал', url = 'https://t.me/salesrf')
site_channek_link_keyboard = InlineKeyboardMarkup().row(site_link_button, channel_link_button)

base_knowlege_keyboard = make_keyboard(texts['keyboards']['faq']['main'])

base_knowlege_pages_keyboard = make_keyboard(texts['keyboards']['faq']['functional'])

faq_keyboard = make_keyboard(texts['keyboards']['faq']['faq'])
