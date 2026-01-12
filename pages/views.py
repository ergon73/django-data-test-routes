from django.http import HttpResponse


def home_page(request):
    return HttpResponse(
        "<h1>Django Routes Project</h1>"
        "<p>Это учебный Django-проект с маршрутами /data/ и /test/</p>"
        "<ul>"
        "<li><a href='/data/'>/data/</a> - страница с данными</li>"
        "<li><a href='/test/'>/test/</a> - тестовая страница</li>"
        "</ul>"
    )


def data_page(request):
    return HttpResponse("<h1>Data page</h1><p>Content for /data</p>")


def test_page(request):
    return HttpResponse("<h1>Test page</h1><p>Content for /test</p>")
