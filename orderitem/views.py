from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from order.models import OrderItem
from .serializers import OrderItemSerializer
from .forms import OrderItemForm
from django_filters.views import FilterView
from .filters import OrderItemFilter


class OrderItemListView(FilterView):
    filterset_class = OrderItemFilter
    queryset = OrderItem.objects.filter()
    template_name = 'orderitem.html'
    paginate_by = 20

class OrderItemCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new orderitem, mixin used to display message
    model = OrderItem  # setting 'OrderItem' model as model
    form_class = OrderItemForm  # setting 'OrderItemForm' form as form
    template_name = "edit_orderitem.html"  # 'edit_orderitem.html' used as the template
    success_url = 'orderitem'  # redirects to 'orderitem' page in the url after submitting the form
    success_message = "OrderItem has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New OrderItem'
        context["savebtn"] = 'Add to OrderItem'
        return context

# ************ Start Of: Inserted as a Test ****************
# @login_required(login_url="/login_user/")
def edit_orderitem(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        orderitem = OrderItem.objects.get(id=request.POST.get('id', ''))
        if orderitem == None:
            return HttpResponse("<h2>OrderItem Not Found</h2>")
        else:

            orderitem.numworkstation = request.POST.get('numworkstation', '')
            orderitem.numserver = request.POST.get('numserver', '')
            orderitem.numipaddress = request.POST.get('numipaddress', '')
            orderitem.nummonths = request.POST.get('nummonths', '')
            orderitem.labordelivery = request.POST.get('labordelivery', '')
            orderitem.save()

            messages.success(request, "Updated Successfully")
            return HttpResponseRedirect("update_orderitem/"+str(orderitem.id)+"")


# ************ End Of: Inserted as a Test ****************

class OrderItemUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit orderitem, mixin used to display message
    model = OrderItem  # setting 'OrderItem' model as model
    form_class = OrderItemForm  # setting 'OrderItemForm' form as form
    template_name = "edit_orderitem.html"  # 'edit_orderitem.html' used as the template
    success_url = '/orderitem'  # redirects to 'orderitem' page in the url after submitting the form
    success_message = "OrderItem has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit OrderItem'
        context["savebtn"] = 'Update OrderItem'
        context["delbtn"] = 'Delete OrderItem'
        return context

class OrderItemDeleteView(View):  # view class to delete orderitem
    template_name = "delete_orderitem.html"  # 'delete_orderitem.html' used as the template
    success_message = "OrderItem has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        return render(request, self.template_name, {'object': orderitem})

    def post(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        orderitem.is_deleted = True
        orderitem.save()
        messages.success(request, self.success_message)
        return redirect('orderitem')

    class OrderItemViewSet(viewsets.ModelViewSet):
        queryset = OrderItem.objects.all().order_by('id')
        serializer_class = OrderItemSerializer
