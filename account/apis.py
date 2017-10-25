from django.http import JsonResponse
from account.models import Profile, Request
from account.serializers import ProfileSerializer, RequestSerializer


def client_get_profiles(request):
    profiles = ProfileSerializer(
        Profile.objects.all(),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'profiles': profiles})


def client_get_request(request, request_id):
    print ('---------------------')
    print ('request_id =' + request_id)
    reqs = RequestSerializer(
        Request.objects.all().filter(id=request_id),
        many=True,
        context={'request': request}
    ).data
    return JsonResponse({'reqs': reqs})
