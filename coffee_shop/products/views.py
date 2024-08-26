from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response


from .forms import ProductForm
from products.models import Product
from .serializer import ProductoSerializer

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = 'list_product.html'
    context_object_name = 'products'

    def get_context_data(self):
        product_list = Product.objects.all()
        return {
            'product_list':product_list
        }
    

class ProductListAPI(APIView):
    authentication_classes = {}
    permission_classes = {}

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductoSerializer(products, many=True)
        return Response(serializer.data)