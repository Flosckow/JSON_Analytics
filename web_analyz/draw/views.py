from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.conf import settings
import plotly.graph_objects as go


class GetJson(APIView):
    l_name = []
    c_name = []
    # динамические поля, для построения графика
    c1_field = ''
    l1_field = ''

    def post(self, request):
        print(request.data)
        if "file" in request.FILES:
            file = request.FILES['file']
            if self.write(file):
                self.draw()
        return HttpResponseRedirect('/lk/render')

    def write(self, file):

        data = json.load(file)
        k = 0
        for i in data:
            self.l_name.append(i['name'])
            self.c_name.append(i['country'])
            k += 1

        return True

    def draw(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.l_name, y=self.c_name))
        fig.update_layout(legend_orientation="h",
                          legend=dict(x=.5, xanchor="center"),
                          title="Plot Title",
                          xaxis_title="name",
                          yaxis_title="country",
                          margin=dict(l=0, r=0, t=30, b=0))
        fig.update_layout(
            autosize=False,
            width=800,
            height=600, )
        fig.write_html(f'{settings.BASE_DIR}/templates/first_figure.html', auto_open=False)


def render_html(request):
    return render(request, 'first_figure.html')


# функция удаляет файл после отрисовки
def delete_test_html(templates):
    pass



