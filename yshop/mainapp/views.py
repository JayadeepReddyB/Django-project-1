from django.shortcuts import render, redirect # helps to render the template , redirect the user if required 
from django.http import HttpResponse # helps us to create a http response object -- responding to the user

from django.template import loader # helps in file handling -- handling thee file 
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all() # querying all records in the DB of entity type `Product`
    # i.e. this translates to the DQL :-> `SELECT * FROM PRODUCT;`
    context = {
        'prods' : products # the key `prods` will now be available  to use in the django template design

    }    # context dictionary for passing data for rendering
    template = loader.get_template('home.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request))  # creates a response object after rendering
    # the returned response has the html of completed webpage including required data.


#view function for rendering individual product page
def product_details(request,id):
    product = Product.objects.get(id = id) # select * from products where id = <parameter_id>
    context = {
            'prod' = product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))

