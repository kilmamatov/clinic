from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.Index.as_view(), name='home'),
    path('doctors/', core.views.DoctorList.as_view(), name='doctors'),
    path('doctor/<int:pk>/', core.views.DoctorDetail.as_view(), name='doctor'),
    path('appeals/', core.views.AppealsList.as_view(), name='appeals'),
    path('appeal/<int:pk>/', core.views.AppealDetail.as_view(), name='appeal'),
    path('addappeal/', core.views.AppealCreate.as_view(), name='addappeal'),
]
