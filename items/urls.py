from django.urls import path
from .views import CreateCheckoutSessionView, ItemBuyView, SuccessView, CancelView

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ItemBuyView.as_view(), name='item-buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]