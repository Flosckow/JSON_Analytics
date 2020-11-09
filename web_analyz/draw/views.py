
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.views import APIView
import json
from django.conf import settings
import plotly.graph_objects as go
import logging
import datetime
import glob
import os

from web_analyz import settings


class GetJson(APIView):
    l_name = []
    c_name = []

    def post(self, request):
        print(request.user)
        x_field = request.data['x_field']
        y_field = request.data['y_field']
        if "file" in request.FILES:
            file = request.FILES['file']
            if self.write(file, x_field, y_field):
                self.draw(x_field, y_field)
        return HttpResponseRedirect('/lk/render')

    def write(self, file, x_field, y_field):

        data = json.load(file)
        k = 0
        for i in data:
            self.l_name.append(i[x_field])
            self.c_name.append(i[y_field])
            k += 1
        return True

    def draw(self, x_field, y_field):
        time_now = datetime.datetime.today().strftime("%Y-%m-%d")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.l_name, y=self.c_name))
        fig.update_layout(legend_orientation="h",
                          legend=dict(x=.5, xanchor="center"),
                          title="Plot Title",
                          xaxis_title=x_field,
                          yaxis_title=y_field,
                          margin=dict(l=0, r=0, t=30, b=0))
        fig.update_layout(
            autosize=False,
            width=800,
            height=600, )
        fig.write_html(f'{settings.BASE_DIR}/templates/{time_now}first_figure.html', auto_open=False)


def search_html():
    os.chdir(f'{settings.BASE_DIR}/templates')
    for file in glob.glob("*.html"):
        readable_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        k = datetime.datetime.now() - readable_time
        if k.days < 1:
            if k.seconds < 144000:
                return file


def render_html(request):
    file = search_html()
    return render(request, file)



# # return redirect('https://wwww.askpython.com')




