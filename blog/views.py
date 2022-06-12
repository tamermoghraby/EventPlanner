from django.shortcuts import *
from blog.models import Blog, Contact 
import math

# Create your views here.
def home(request):
	return render(request, 'index.html')

def blog(request):
	no_of_posts = 5
	page = request.GET.get('page')
	if page is None:
		page = 1

	else:
		page = int(page)

	blogs = Blog.objects.all()
	length = len(blogs)
	blogs = blogs[(page-1)*no_of_posts : page*no_of_posts]

	if page > 1 :
		prev = page-1

	else:
		prev = None

	if page < math.ceil(length/no_of_posts):
		nxt = page+1

	else:
		nxt = None
	

	print(prev, nxt)
	context = {'blogs': blogs, 'prev': prev, 'nxt': nxt, }
	return render(request, 'bloghome.html', context)

def contact(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		desc = request.POST.get("desc")
		instance = Contact(name = name, email = email, phone = phone, desc = desc)
		instance.save()
	return render(request, 'contact.html', )


def blogpost(request, slug):
	blog = Blog.objects.filter(slug=slug).first()
	context = {'blog':blog}
	return render(request, 'blogpost.html', context)

def search(request):
	return render(request, 'search.html')

def scorecounter(ops):

	ops = ["5", "2", "C", "D", "+"]
	score = 0
	list = []

	for x in ops:

		if isinstance(x,int):
			list.append(ops[x])

		elif x == "D":
			num = list[-1] * 2
			list.append(num)

		elif x == "C":
			list.pop(x)

		elif x == "+":
			num = list[-1]+list[-2]
			list.append(num)

		else:
			pass


	for z in list:
		score = score + int(z)

	return score 
	



		
	

