from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts_list(request):
		n = ['peter', '50cnt', 'pit']
		return render(request, 'school/index.html', context={'names': n})	

def inter(request):
		return render(request, 'school/inter.html')		

def pre(request):
		return render(request, 'school/pre.html')		

def elementary(request):
		return render(request, 'school/elementary.html')	


def modal(request):
		return render(request, 'school/modal.html')			

# Elementary Listening
def elm_1(request):
		return render(request, 'school/elm/listening/text_one.html') 

# Elementary Grammar		
def gram_1(request):
		return render(request, 'school/elm/grammar/gram_1.html')

def gram_2(request):
		return render(request, 'school/elm/grammar/gram_2.html')


def gram_3(request):
		return render(request, 'school/elm/grammar/gram_3.html')

def gram_4(request):
		return render(request, 'school/elm/grammar/gram_4.html')	
			
def gram_5(request):
		return render(request, 'school/elm/grammar/gram_5.html')

def gram_6(request):
		return render(request, 'school/elm/grammar/gram_6.html')		

def gram_7(request):
		return render(request, 'school/elm/grammar/gram_7.html')		

def gram_8(request):
		return render(request, 'school/elm/grammar/gram_8.html')				



# Elementary Vocabulary	
def vocabulary_1(request):
		return render(request, 'school/elm/vocabulary/vocabulary_1.html')

def vocabulary_2(request):
		return render(request, 'school/elm/vocabulary/vocabulary_2.html')

