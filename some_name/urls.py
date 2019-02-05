from django.conf.urls import url
from . import views
from some_name.views import userView,userSum

urlpatterns = [
    #url(r'^$',views.current_datetime,name = 'home')

    # url(r'^pv', paymentView.as_view() , name='PaymentView')

    url(r'^$', views.home, name='home'),
    url(r'^payment', views.paymentView.as_view(), name='payment'),
    url(r'pay', views.paymentView.as_view(), name='pay'),

    url(r'^user', views.userView.as_view(), name = 'user'),
    url(r'^usum', views.userSum.as_view(), name='usersum'),
    url(r'usucess',view.userSucess.as_view(),name='usersuccess')
]