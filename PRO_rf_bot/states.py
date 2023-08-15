from aiogram.utils.helper import Helper, HelperMode, ListItem, Item


class States(Helper):
    mode = HelperMode.snake_case

    MAIN = Item()
    FAQ_MAIN = Item()
    FAQ_FAQ = Item()
    FAQ_FUNCTIONAL = Item()


if __name__ == '__main__':
    print(States.all())