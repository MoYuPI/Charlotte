from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from spiders.models import NewHouse
from spiders.serializers import NewHouseDetailSerializer, NewHouseListSerializer


# Create your views here.
@csrf_exempt
def newhouse_list(request):
    """
    List all code newhouses, or create a new house.
    """
    try:
        page_size = int(request.GET.get('page_size', 10))
        page = int(request.GET.get('page', 1))
    except (TypeError, ValueError):
        return JsonResponse(code=status.HTTP_400_BAD_REQUEST, desc='page and page_size must be integer!')


    if request.method == 'GET':
        houses = NewHouse.objects.all()
        print(page_size)
        paginator = Paginator(houses, page_size)
        total = paginator.num_pages
        try:
            houses = paginator.page(page)
        except PageNotAnInteger:
            houses = paginator.page(1)
        except EmptyPage:
            houses = paginator.page(paginator.num_pages)
        serializer = NewHouseListSerializer(houses, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return JsonResponse({
                'data': serializer.data,
                'page': page,
                'total': total
            })  # 返回

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewHouseListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def newhouse_detail(request, pk):
    """
    Retrieve, update or delete a code newhouse.
    """
    try:
        newhouse = NewHouse.objects.get(pk=pk)
    except NewHouse.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewHouseDetailSerializer(newhouse)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewHouseDetailSerializer(newhouse, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        newhouse.delete()
        return HttpResponse(status=204)