
# @class_declaration web #
from django.shortcuts import render


class web(yblogin):

    def web_index(self, request):
        return render(request, "portal/home.html", {})

    def web_catalogue(self, request):
        return render(request, "portal/catalogue.html", {})

    def web_product(self, request):
        return render(request, "portal/product.html", {})

    def __init__(self, context=None):
        super().__init__(context)

    def index(self, request):
        return self.ctx.web_index(request)

    def catalogue(self, request):
        return self.ctx.web_catalogue(request)

    def product(self, request):
        return self.ctx.web_product(request)
