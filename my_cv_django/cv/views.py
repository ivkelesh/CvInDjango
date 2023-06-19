from django.shortcuts import render, get_object_or_404
from django.views import View

from cv.models import Cv


class CvView(View):
    template_name = 'my_cv.html'
    list_template_name = 'cv_list.html'

    def get(self, request, id=None):
        tempalte = self.template_name
        if id:
            cv = get_object_or_404(Cv, id=id)

            context = {
                'cv': cv,
                "experiences": cv.experiences.all(),
                "skills": cv.skills.all(),
                "educations": cv.educations.all(),
                "contacts": cv.contacts.all(),
            }
        else:
            cvies = Cv.objects.all()
            tempalte = self.list_template_name
            context = {
                'cvies' : cvies,
            }

        return render(request, tempalte, context)
