from django.shortcuts import render, get_object_or_404
from django.views import View

from cv.models import Cv


class CvView(View):
    template_name = 'my_cv.html'

    def get(self, request, id):
        cv = get_object_or_404(Cv, id=id)
        return render(request, self.template_name, {'cv': cv})
