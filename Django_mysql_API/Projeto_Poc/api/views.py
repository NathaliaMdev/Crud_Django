import json
from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from .models import ProducerItem
from django.views.decorators.csrf import csrf_exempt

#Create your views here.
#@csrf_exempt
class ProducerItemView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if (id>0):
            producerItems = list(ProducerItem.objects.filter(id=id).values())
            if len(producerItems) >0:
                produtorItems = producerItems[0]
                dados={'message':"Sucess",'ProducerItems':producerItems}
            else:
                dados={'message':'ProducerItems not found...'}
            return JsonResponse(dados)
        producerItems=list(ProducerItem.objects.values())
        if len(producerItems)>0:
            dados={'message':"Sucess",'ProducerItems':producerItems}
        else:
            dados={'message':'ProducerItems not found...'}
        return JsonResponse(dados)
    def post(self,request):
        #print(reques,body)
        jd=json.loads(request.body)
        print(jd)
        ProducerItem.objects.create(name=jd['name'], created_at=jd['created_at'], updated_at=jd['updated_at'],value=jd['value'])
        #print(jd)
        return JsonResponse({'message':'Sucess'})
    def put(self, request, id):
        jd = json.loads(request.body)
        producerItems = list(ProducerItem.objects.filter(id=id).values())
        if len(producerItems) >0:
            produtoritem = ProducerItem.objects.get(id=id)
            produtoritem.name=jd['name']
            produtoritem.created_at=jd['created_at']
            produtoritem.updated_at=jd['updated_at']
            produtoritem.value=jd['value']
            produtoritem.save()
            dados = {'message': "Sucess"}
        else:
            dados = {'message:"Product not found...'}
        return JsonResponse(dados)
    def delete(self,request, id):
        produtoritem = list(ProducerItem.objects.filter(id=id).values())
        if len(produtoritem)>0:
            ProducerItem.objects.filter(id=id).delete()
            dados = {'message':"Sucess"}
        else:
            dados = {'message': "Company not found..."}
        return JsonResponse(dados)