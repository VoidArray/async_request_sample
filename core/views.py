import random
from time import sleep

from django.views.generic import View
from django.http import JsonResponse


class JResponseView(View):

    def get(self, request, *args, **kwargs):
        results = []
        common_range = list(kwargs['range_1st']) + list(kwargs['range_2nd'])
        for num_id in common_range:
            results.append({'id': str(num_id), 'name': 'my name %s' % num_id})
        timeout = random.randint(10, 35) / 10  # noise maker
        print(timeout)
        sleep(timeout)
        return JsonResponse(results, safe=False)

