from tools import DataBase

db = DataBase(
    host='95.154.68.63',
    port=3306,
    user='student',
    password='Hn523cv-',
    db='Prodivers_LD_DB',
)


def get_data_product():
    print('Введите id продукта для получения информации: ')
    input