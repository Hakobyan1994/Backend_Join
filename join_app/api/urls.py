from django.urls import path
from .views import CreateContactList,CreateContactDetail,CreateTasksList,CreateTasksDetail
 


# Path-Urls 
urlpatterns = [
      path('create_contacts/',CreateContactList.as_view(),name='create_contacts'),
      path('create_contacts/<int:pk>',CreateContactDetail.as_view(),name='contact_detail'),
      path('create_tasks/',CreateTasksList.as_view(),name='create_tasks'),
      path('create_tasks/<int:pk>',CreateTasksDetail.as_view(),name='task_detail')
]


