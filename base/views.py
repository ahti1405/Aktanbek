import csv

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

from django.conf import settings
from django.views import View
from django.http import Http404, HttpResponse
import os
# Create your views here.



class HomePageView(ListView):
    model = Category
    template_name = 'index_1.html'
    context_object_name = 'categories'


class ProductsPageView(DetailView):
    model = Category
    template_name = 'products.html'
    context_object_name = 'category'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
   

class PortfolioView(DetailView):
    model = Product
    template_name = 'portfolio-details.html'
    context_object_name = 'product'
    
# class TestView(ListView):
#     model = Category
#     template_name = 'test.html'
#     context_object_name = 'categories'

"""
How to use this view ?
----------------------
class YourFileDownloadView(FileDownloadView):
    folder_path = 'path of the folder where the file is'
    file_name = 'name of the file to be downloaded'
    content_type_value = 'content type used for the format of `file_name`'
"""




# class FileDownloadView(View):
#     # Set FILE_STORAGE_PATH value in settings.py
#     folder_path = settings.FILE_STORAGE_PATH
#     # Here set the name of the file with extension
#     file_name = 'file.csv'
#     # Set the content type value
#     content_type_value = 'text/plain'

#     def get(self,request):
#         # self.file_name = file_name
#         file_path = 'data/file.csv'
#         if os.path.exists(file_path):
#             with open(file_path, 'rb') as fh:
#                 response = HttpResponse(
#                     fh.read(),
#                     content_type=self.content_type_value
#                 )
#                 response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#         else:
#             raise Http404

def csv_view(request, pk):
   
    product = Product.objects.get(id=pk)
    table = product.table

    with open(f'{table}') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    return render(request, 'csv.html', {'items':items, 'product':product, 'table': table}) # will remove 'table' then