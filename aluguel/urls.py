from django.urls import path
from .views import listar_carros, realizar_aluguel, detalhar_car, realizar_aluguel_car,cadastrar_cliente,cadastrar_car

urlpatterns = [
    path('carros/', listar_carros, name='listar_carros'),
    path('car/<int:pk>', detalhar_car, name='detalhar_car'),
    path('car/aluguel/<int:car_pk>', realizar_aluguel_car, name='realizar_aluguel_car' ),
    path('car/add',cadastrar_car, name='cadastrar_carro'),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
    path('clientes/add',cadastrar_cliente, name='cadastrar_cliente')
    
]