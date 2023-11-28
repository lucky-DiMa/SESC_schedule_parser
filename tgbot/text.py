from models.db import DB
from models.models import columns_json


# порядок ввода: tuple(краткое имя, русское вариант, англиский вариант) ......
class TextMessage:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *args):
        self.__text = self.__args_to_dict(args)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        raise 'You can not change this attribute'

    @classmethod
    def __args_to_dict(cls, arguments: tuple):
        res = {'ru': {},
               'en': {}
               }

        for i in arguments:
            for index, value in enumerate(i):
                if index % 3 == 1:
                    res['ru'][i[0]] = value
                elif index % 3 == 2:
                    res['en'][i[0]] = value
                else:
                    continue
        return res

    async def __call__(self, short_name_text_mes: str, user_id: int):
        session = DB()
        await session.connect()
        lang = await session.select_user_by_id(user_id)
        lang = lang[columns_json[3]]
        return self.__text[lang][short_name_text_mes]


TEXT = TextMessage(('hello', 'Привет! Это бот, котрый может показать тебе актуальное расписание у любого класса и на '
                             'любой день в СУНЦ УрФУ!', 'Hi! This is a bot that can show you the current schedule for '
                                                        'any class and on any day in SESC UrFU!'),
                   ('choose_role', 'Выберите Вашу роль', 'Choose your role'),
                   ('disciple', 'Ученик', 'Student'),
                   ('teacher', 'Учитель', 'Teacher'),
                   ('parents', 'Родитель', 'Parent'))
