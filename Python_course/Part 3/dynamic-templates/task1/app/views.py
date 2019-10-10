import csv
from django.shortcuts import render
from django.views.generic import TemplateView
from app.settings import INFLATION_CSV


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        inflation_color = []
        headers = []
        with open(INFLATION_CSV, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            flag = True
            for row in reader:
                year = []
                keys = row.keys()

                for key in keys:
                    month = {}
                    if row[key]:
                        if key == 'Год':
                            month['count'] = int(row[key])
                        else:
                            month['count'] = float(row[key])

                        if month['count'] < 0:
                            month['color'] = 'green'

                        elif 1 <= month['count'] < 2:
                            month['color'] = 'orangered'

                        elif 2 <= month['count'] < 5:
                            month['color'] = 'red'
                        elif month['count'] >= 5:
                            month['color'] = 'darkred'
                        else:
                            month['color'] = 'white'

                        if key == 'Год':
                            month['color'] = 'white'

                        elif key == 'Суммарная':
                            month['color'] = 'lightgrey'

                    else:
                        month['count'] = '-'
                        month['color'] = 'white'

                    year.append(month)

                    if flag:
                        headers.append(key)

                flag = False
                inflation_color.append(year)

        context = {'data': inflation_color, 'headers': headers}
        return render(request, self.template_name,
                      context)
