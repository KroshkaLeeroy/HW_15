import json
import sqlite3
import flask

app = flask.Flask(__name__)


def get_dy_index(index):
    with sqlite3.connect("animal.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(f'''select 'index', age_upon_outcome, at2.animal, c.color 
                                        FROM my_table mt
                                        join animal_type at2 
                                        join color c 
                                        join color2
                                        where "index" = {index}''').fetchone()

        return dict(result)


@app.get('/<itemid>')
def response(itemid):
    return app.response_class(response=
                              json.dumps(get_dy_index(itemid), ensure_ascii=False),
                              status=200,
                              mimetype='application/json'
                              )


if __name__ == '__main__':
    app.run()

# sql = 'INSERT INTO  color(id, color) values'
#
# for color in ['white', 'black', 'orange', 'blue', 'seal', 'brown', 'blue cream', 'lynx', 'red', 'cream', 'gray', 'buff', 'chocolate', 'silver', 'flame', 'tan', 'apricot', 'yellow', 'lilac']:
#     sql += f'("{color}", "{color}"),'
#
# sql = sql[:-1]
# print(sql)
#
# sql = """
# SELECT *
# FROM color c
# """

# with sqlite3.connect("animal.db") as connection:
#         connection.row_factory = sqlite3.Row
#         result = connection.execute(f'''
#                                     SELECT *
#                                     FROM color c
#                                     ''').fetchall()
#         for i in result:
#             value = dict(i)
#
#             connection.execute(f'''
#             update my_table
#             set color1 = {value['id']}
#             where color1 = '{value["color"]}'
#             ''' )