Приложение pay_service содержит settings.py . items содержит методы stripe API. 
В разделе views.py в классе CreateCheckoutSessionView реализована функция, выдающая session.id методом stripe.checkout.Session.create(...).
Класс ItemBuyView реализует простейшую html страничку и кнопку buy. Рендерится item_buy.html, в теге script на javascript реализован stripe.redirectToCheckout.
Из дополнительных задач выполнен просмотр Django моделей в Django Admin.
ВАЖНО: выбор предмета осуществляется внутри item = Item.objects.get(name="Test Item"). Только так смог реализовать выбор предмета, нужно менять имя в этом queryset.
