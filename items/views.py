from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Item
import stripe

stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY
class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[
                {
                    'name': item.name,
                    'description': item.description,
                    'price': item.price,
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url =DOMAIN + '/cancel/',


        )
        return JsonResponse({
            'id': checkout_session.id
        })

class ItemBuyView(TemplateView):
    template_name = 'items/item_buy.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="Test Item")
        context = super(ItemBuyView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY
        })
        return context

class SuccessView(TemplateView):
    template_name = 'items/success.html'

class CancelView(TemplateView):
    template_name = 'items/cancel.html'