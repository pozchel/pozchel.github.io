from django.urls import path
from .views import *

urlpatterns = [ 
	path('', posts_list, name='posts_lists_url'),
	path('school/inter', inter, name='inter_url'),
	path('school/elementary', elementary, name='elementary_url'),
	path('school/pre', pre, name='pre_url'),
	path('school/modal', modal, name='modal_url'),

	path('school/elm_1', elm_1, name='elm_1_url'),
	path('school/gram_2', gram_2, name='gram_2_url'),

	path('school/gram_1', gram_1, name='gram_1_url'),
	path('school/gram_2', gram_2, name='gram_2_url'),
	path('school/gram_3', gram_3, name='gram_3_url'),
	path('school/gram_4', gram_4, name='gram_4_url'),
	path('school/gram_5', gram_5, name='gram_5_url'),
	path('school/gram_6', gram_6, name='gram_6_url'),
	path('school/gram_7', gram_7, name='gram_7_url'),
	path('school/gram_8', gram_8, name='gram_8_url'),

	path('school/vocabulary_1', vocabulary_1, name='vocabulary_1_url'),
  path('school/vocabulary_2', vocabulary_2, name='vocabulary_2_url'),

]