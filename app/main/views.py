from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bloomify - Главная'
        context['content'] = "Bloomify"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bloomify - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный, и какой хороший товар."
        return context


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bloomify - Контакты'
        context['content'] = "Контакты"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный, и какой хороший товар."
        return context

class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bloomify - Оплата и доставка'
        context['content'] = "Доставка"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный, и какой хороший товар."
        return context
