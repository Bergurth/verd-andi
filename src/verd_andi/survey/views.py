from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.utils import timezone
from .models import Survey

# Create your views here.
# Create your views here.
def index(request):
        return HttpResponse("Hello, world. You're at the survey index.")




class SurveyListView(ListView):
	model = Survey

	def get_context_data(self, **kwargs):
		context = super(SurveyListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class SurveyDetailView(DetailView):
	model = Survey

	def get_context_data(self, **kwargs):
		context = super(SurveyDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		print(str(context))
		return context



# def survey(request):
# 	if request.user.is_authenticated():

# 		org_qs = Org.objects.filter(members=request.user.id).order_by('name')

# 		context = {

# 			"user_name": str(request.user),
# 			"user_id": str(request.user.id),
# 			"orgs": org_qs,
# 		}
	
# 		return render(request, "user_dash.html", context)
# 	else:
# 		return redirect(settings.LOGIN_REDIRECT_URL)


def survey_dash(request, id):
	if request.user.is_authenticated():

		context = {
			"user_name" : str(request.user),
			"user_id" : str(request.user.id),
		}

		return render(request, "survey/survey_dash.html", context)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)