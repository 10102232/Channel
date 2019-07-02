from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    name = '签到哥'
    d1 = {
        'name': '签到哥',
        'hobby': '签到',
        'info': '人畜无害',
        'items': '呵呵'
    }
    l1 = ['签到哥', '闷骚哥', '黄袍哥', '戴帽哥']

    print(l1[0])

    class Person(object):
        def __init__(self, name, age, dream):
            self.name = name
            self.age = age
            self.dream = dream

        def dream(self):
            return '我有一个梦想！我能反杀！'

    p1 = Person('康抻', 49, '白日梦')

    name2 = 'ALEX'
    file_size = 1234

    now = datetime.datetime.now()
    now = now - datetime.timedelta(days=7)

    # a_html = '<a href="https://www.luffycity.com">路飞学城</a>'
    a_html = '<script>alert(123)</script>'

    s1 = '世情薄人情恶雨送黄昏花易落'
    s2 = 'hello ! hello! How are you? I\'m fine! Thank you!'

    return render(request, 'index.html', {
        'name': name,
        'd1': d1,
        'l1': l1,
        'p1': p1,
        'name2': name2,
        's14': '好',
        'fize_size': file_size,
        'now': now,
        'a_html': a_html,
        's1': s1,
        's2': s2
    })
