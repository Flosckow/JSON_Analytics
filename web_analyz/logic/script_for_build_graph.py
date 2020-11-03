# import json
# import plotly.graph_objects as go
# # append collection
# # вытскиваем данные по индексу и добавляем датасет, как основной ключ
# # как передавать заголовки выборочно, не хардкодить? через инпуты, в которых пользователь вписывает нужные ему поля?
#
# # x = input('Введите нужное поле по оси x: ')
# # y = input('Введите нужное поле по оси y: ')
# # через form
#
# l_name = []
# c_name = []
#
# # def write(data), где data это наш json файл
# def write():
#     with open("test.json", "r") as read_file:
#         data = json.load(read_file)
#         k = 0
#
#         for i in data:
#             l_name.append(i['name'])
#             c_name.append(i['country'])
#             k += 1
#
#
# def draw():
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=l_name, y=c_name))
#     fig.update_layout(legend_orientation="h",
#                     legend=dict(x=.5, xanchor="center"),
#                     title="Plot Title",
#                     xaxis_title="name",
#                     yaxis_title="country",
#                     margin=dict(l=0, r=0, t=30, b=0))
#     fig.update_layout(
#         autosize=False,
#         width=400,
#         height=400,)
#     fig.write_html('first_figure.html', auto_open=False)
#
# write()
# draw()
#
# # Добавитьтри графика, с помощью django/render/temoplate валидирвоать