# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration web #
from django.shortcuts import render


class web(interna):

    def web_index(self, request):
        return render(request, "portal/home.html", {})

    def web_catalogue(self, request):
        return render(request, "portal/catalogue.html", {})

    def web_product(self, request):
        return render(request, "portal/product.html", {})

    def __init__(self, context=None):
        super(web, self).__init__(context)

    def index(self, request):
        return self.ctx.web_index(request)

    def catalogue(self, request):
        return self.ctx.web_catalogue(request)

    def product(self, request):
        return self.ctx.web_product(request)


# @class_declaration head #
class head(web):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
