from django.urls import path
from .views import ProducerItemView

urlpatterns = [
        path('producerItem/', ProducerItemView.as_view(), name='producerItem_list'),
        path('producerItem/<int:id>', ProducerItemView.as_view(), name='producerItem_process')

]

#urlpatterns = [
     #  path('producerItem/', ProducerItemView.ProducerItem, name='producerItem_list'),
     #  path('producerItem/<int:id>', ProducerItemView.ProducerItem, name='producerItem_process')

#]