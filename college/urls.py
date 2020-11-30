from django.urls import path
from . import views

app_name = 'college'
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:category_id>/', views.year_list, name='year_list'),
    path('subject/<int:year_id>/', views.subject_list, name='subject'),  
    path('subject_detail/<int:subject_id>/', views.subject_detail, name='subject_detail'), 
    path('material_paper/<int:subject_id>/', views.paper_list, name='material_paper'),   
    path('material_notes/<int:subject_id>/', views.notes_list, name='material_notes'),
    path('material_video/<int:subject_id>/', views.video_list, name='material_video'),   
    path('paper_create/', views.paper_create_view, name='paper_create'),
    path('notes_create/', views.notes_create_view, name='notes_create'),
    path('video_create/', views.video_create_view, name='video_create'),
    path('paper_list/', views.paper_list_view, name='paper_list'),
    path('paper_approved/<int:paper_id>/', views.paper_approved_view, name='paper_approved'),
    
 
]