from django.shortcuts import render
from django.views.generic import View,TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .form import mainform
from .models import riskdata

class adddataview(View):
    error=None
    def get(self,request):
        print(request.GET.get('wir'))
        return render(request,"adddata.html",{})
    def post(self,request):

        form = mainform(request.POST or None)
        if form.is_valid():
            print(type(form.cleaned_data.get("consequence")))
            obj=riskdata.objects.create(
                risk=form.cleaned_data.get("risk"),
                riskdesc = form.cleaned_data.get("riskdesc"),
                risksol = form.cleaned_data.get("risksol"),
                consequence = form.cleaned_data.get("consequence"),
                likelihood = form.cleaned_data.get("likelihood")
            )
#            print(form.cleaned_data.get("consequence"))

        if form.errors:
            self.error=form.errors
            print(form.errors)
        return render(request, "adddata.html", {"error":self.error})


def homepage(request):
    return render(request,'index.html',{})

class charts(View):
    def get(self,request):
        return render(request,'displaychart.html',{})


class chartdata(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,format=None):
        lables = []
        datavalues = []
        obj=riskdata.objects.all()
        for ele in obj:
            if ((ele.risk) and (ele.consequence) and (ele.likelihood)):
                lables.append(ele.risk)
                datavalues.append(int(ele.consequence)*int(ele.likelihood))
        print(lables)
        print(datavalues)
        data={"lables":lables,"datavalues":datavalues}
        return Response(data)
