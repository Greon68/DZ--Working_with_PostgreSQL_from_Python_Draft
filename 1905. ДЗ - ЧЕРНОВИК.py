# Домашнее задание к лекции «Работа с PostgreSQL из Python»
# Создайте программу для управления клиентами на Python.
#
# Требуется хранить персональную информацию о клиентах:
#
# имя,
# фамилия,
# email,
# телефон.
# Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше.
# А может и вообще не быть телефона, например, он не захотел его оставлять.
#
# Вам необходимо разработать структуру БД для хранения информации и несколько функций
# на Python для управления данными.
#
# 1)Функция, создающая структуру БД (таблицы).
# 2)Функция, позволяющая добавить нового клиента.
# 3)Функция, позволяющая добавить телефон для существующего клиента.
# 4)Функция, позволяющая изменить данные о клиенте.
# 5)Функция, позволяющая удалить телефон для существующего клиента.
# 6)Функция, позволяющая удалить существующего клиента.
# 7)Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.

# Каркас кода
# import psycopg2
#
# def create_db(conn):
#     pass
#
# def add_client(conn, first_name, last_name, email, phones=None):
#     pass
#
# def add_phone(conn, client_id, phone):
#     pass
#
# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     pass
#
# def delete_phone(conn, client_id, phone):
#     pass
#
# def delete_client(conn, client_id):
#     pass
#
# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     pass
#
#
# with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
#     pass  # вызывайте функции здесь
#
# conn.close()


# Внвчале создадим базу данных client и подключимся к ней.
# Пароль для подключения - личный
import psycopg2




with psycopg2.connect(database="client", user="postgres", password="Greon68Taganrog2023") as conn:
    with conn.cursor() as cur:
        #удаление таблиц
        cur.execute("""
               DROP TABLE phones;
               DROP TABLE clients;
               """)

        # 1)Функция, создающая структуру БД (таблицы).
        def creating_tables (cursor):
            # создание таблицы client
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                    client_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(60) NOT NULL ,
                    last_name VARCHAR(60) NOT NULL ,
                    email VARCHAR(120) UNIQUE NOT NULL 
                    );
                """)
            # создание таблицы телефонов
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS phones (
                    phone_id SERIAL PRIMARY KEY,
                    client_id  INTEGER NOT NULL REFERENCES clients(client_id),
                    number INTEGER 
                    );
                """)
            conn.commit()  # фиксируем в БД


        tables= creating_tables(cur)



        # # 2) Функция, позволяющая добавить нового клиента.
        # # def add_client(conn, first_name, last_name, email, phones=None):
        #
        # # Добавим без функции
        cur.execute("""
            INSERT INTO clients (first_name, last_name, email )
            VALUES (%s, %s, %s);
            """ , ('Ivan','Petrov', 'ivan@python.com'))
        conn.commit()

        #
        # # def get_course_id(cursor, name: str):
        # #     cursor.execute("""
        # #                SELECT id FROM course
        # #                WHERE name=%s;
        # #                """, (name,))
        # #     return cursor.fetchone()[0]
        # #
        # #
        # # python_id = get_course_id(cur, 'Python')
        # # print('python_id -', python_id)
        #
        # 2) Функция, позволяющая добавить нового клиента.
        def add_client(cursor, first_name, last_name, email):
            cursor.execute("""
            INSERT INTO clients (first_name, last_name, email )
            VALUES (%s, %s, %s);
            """ , (first_name, last_name, email ))


        client_2 = add_client ( cur ,'Petr','Ivanov', 'petr@python.com')
        client_3 =  add_client ( cur ,'Anton','Vasin', 'anton@python.com')
        client_4 =  add_client ( cur ,'Igor','Valin', 'ig@python.com')
        client_5 = add_client(cur, 'Irina', 'Li', 'li@python.com')
        client_6 = add_client(cur, 'Serg', 'Valin', 'se@python.com')
        client_7 = add_client(cur, 'Serg', 'Sun', 'sun@python.com')
        # 3)Функция, позволяющая добавить телефон для существующего клиента

        # Добавим без функции новую строку в табл. phones
        cur.execute("""
            INSERT INTO phones (client_id, number)
            VALUES (%s, %s );
            """ , (1,33322233))

        conn.commit()

        # Добавление через функцию :
        def add_phone(cursor, client_id, number=None):
            cursor.execute("""
                        INSERT INTO phones (client_id, number)
                        VALUES (%s, %s );
                        """, (client_id, number))

        phone_2 = add_phone(cur,1,22233322)
        phone_3 = add_phone(cur,2)
        phone_4 = add_phone(cur, 3, 11122233)
        phone_5 = add_phone(cur, 3, 11122234)
        phone_6 = add_phone(cur, 4, 55522233)
        phone_7 = add_phone(cur, 5, 11100077)
        phone_8 = add_phone(cur, 6, 10203040 )
        phone_9 = add_phone(cur, 7, 7770088)


        # 5)Функция, позволяющая удалить телефон для существующего клиента.

        # Без функции .Удалим телефон клиента с id=4
        # cur.execute("""
        #     DELETE FROM  phones WHERE client_id=%s;
        #     """, (4,))
        # cur.execute("""
        #         SELECT * FROM phones;
        #         """)
        # print(cur.fetchall())

        # Удаление через функцию
        def delete_phone (cursor,client_id):
            cursor.execute("""
            DELETE FROM  phones WHERE client_id=%s;    
            """, (client_id ,))

        # client_delete_phone_1 = delete_phone ( cur, 3 )


       # 6) Функция, позволяющая удалить существующего клиента.

        # Без функции . Удалим пользователя с id=3
        # cur.execute("""
        #        DELETE FROM  clients WHERE client_id=%s;
        #          """, (3,))
        # conn.commit()
        def delete_client(cursor, client_id):
            delete_phone(cursor, client_id)
            cursor.execute("""
                    DELETE FROM  clients WHERE client_id=%s;    
                    """, (client_id,))


        # client_delete_1 = delete_client (cur,3)



        # 4.Функция, позволяющая изменить данные о клиенте .




        def new_data3(cursor, client_id, first_name=None, last_name=None, email=None):
            # Сформируем словарь 'название входного элемента':'значение входного элемента'
            data_in_dict = {'first_name': first_name, 'last_name': last_name, 'email': email, 'client_id': client_id}

            # Создадим возможность внесения изменений независимо друг от друга

            data = []  # рабочий список входных параметров
            data_in = []  # список входных параметров
            data_out_0 = []  # Список выходных параметров
            for x, y in data_in_dict.items():
                if y != None:
                    z = f'{x}=%s'
                    data.append(z)
                    data_out_0.append(y)
            # Удалим id из списка входных данных
            # print (data)
            data = data [:-1]
            data_in = ", ".join(data)  # строка входных данных
            data_out = tuple(data_out_0)  # кортеж выходных данных

            # print(data_in)
            # print(data_out)

            cursor.execute(f"""
                        UPDATE clients SET {data_in} WHERE client_id=%s;
                        """, data_out)


        new_client = new_data3(cur, 1, 'Ivanko', 'Zuev', None)
        #
        # cur.execute(""" Select * From clients;""")
        # print(cur.fetchall())

        # 7) Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону

        def find_client2(cursor, number):
            ''' Функция определяет id клиента
             по номеру его телефона '''
            cursor.execute("""
                     SELECT cl.client_id FROM clients cl
                     JOIN phones ph ON cl.client_id = ph.client_id
                     WHERE  number=%s ;
                     """, (number,))
            return cursor.fetchone()[0]


        required_client_1 = find_client2(cur, 55522233)
        print(required_client_1)


        def find_client2(cursor,first_name='%', last_name='%',email='%', number=None):
            ''' Функция определяет id клиента
            по одному из параметров - имени , фамилии , адресу электронной почты ,
            либо номеру его телефона '''

            cursor.execute("""
                SELECT cl.client_id FROM clients cl
                JOIN phones ph ON cl.client_id = ph.client_id
                WHERE first_name=%s OR last_name=%s OR email=%s OR number=%s ;
                """, (first_name,last_name,email,number,))
            return cursor.fetchone()[0]


        # cur.execute(""" Select * From clients;""")
        # print(cur.fetchall())
        #
        # required_client_1 = find_client2(cur,'Serg','Sun','',)
        # print (required_client_1)

        def find_client3(cursor,first_name=None, last_name=None,email=None, number=None):
            ''' Функция определяет id клиента
            по одному из параметров - имени , фамилии , адресу электронной почты ,
            либо номеру его телефона '''

            # # Сформируем словарь 'название входного элемента':'значение входного элемента'
            # data_in_dict = {'first_name': first_name, 'last_name': last_name, 'email': email, 'number': number}
            #
            # # Создадим возможность внесения изменений независимо друг от друга
            #
            # data = []  # рабочий список входных параметров
            # data_out_0 = []  # Список выходных параметров
            # for x, y in data_in_dict.items():
            #     if y != None:
            #         z = f'{x}=%s'
            #         data.append(z)
            #         data_out_0.append(y)
            #
            # data_in = ", ".join(data)  # строка входных данных
            # data_out = tuple(data_out_0)  # кортеж выходных данных
            #
            # print(data_in)
            # print(data_out)

            cursor.execute("""
                SELECT cl.client_id FROM clients cl
                JOIN phones ph ON cl.client_id = ph.client_id
                WHERE first_name=%s OR last_name=%s OR email=%s OR number=%s ;
                """, (first_name,last_name,email,number,))

            return cursor.fetchone()[0]

        cur.execute(""" Select * From clients;""")
        print(cur.fetchall())

        required_client_1 = find_client3(cur,'Serg','Sun', 'sun@python.com',10203040)
        print (required_client_1)


conn.close()

