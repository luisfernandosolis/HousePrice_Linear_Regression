from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
import joblib


with open("D:\Proyectos\Python Scripts\Projects\Estimacion de precios de casa\LinearRegression\MLModels\model_joblib","rb") as f:
    model = joblib.load(f)
print(model)


class ModelRegression(APIView):
    def get(self,request):
        return render(request,"form.html",{})
    def post(self,request):
        data=request.data.get("input_value")
        result=model.predict([[float(data)]])
        return render(request, "form.html", {"data":result[0]})
