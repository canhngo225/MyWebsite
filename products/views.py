from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class AddNewProduct(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        return render(request, "products/addNewProduct.html")
