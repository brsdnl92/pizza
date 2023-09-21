from django.http import HttpResponse, JsonResponse
from .models import Pizza

# Create your views here.
# REST API - request-ekhez hozzárendeljük a tevékenységet (ez csak GET kérést kezel)
def hello(request):
    return HttpResponse("<h1>Hello Világ!</h1>")


def getPizzas(request):
    pizzas = Pizza.objects.all()

    li = []

    for pizza in pizzas:
        li.append(pizza.serializer())

    return JsonResponse({"data":li})




