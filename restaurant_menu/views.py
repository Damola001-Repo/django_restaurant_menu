from django.shortcuts import render
from django.views import generic
from .models import Item, CATEGORIES


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = CATEGORIES
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item.html"