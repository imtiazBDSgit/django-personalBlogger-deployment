from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def post_list(request,**kwargs):
    posts = Post.published.all()
    paginator = Paginator(posts, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    posts_page = paginator.get_page(page)
    return render(request,'blog/post/list.html',{'posts':posts_page})

def index(request,**kwargs):
    return render(request,'blog/post/index.html')

def about(request,**kwargs):
    return render(request,'blog/post/about.html')

def thankYou(request,**kwargs):
    return render(request,'blog/post/thankYou.html')

def contact(request,**kwargs):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            form_content = request.POST.get('message', '')
            contact_number = request.POST.get('phone', '')
            try:
                print("the sender email : ",contact_email)
                send_mail(subject=contact_email, message=form_content, from_email=contact_email, recipient_list=['imtiaz.khan.engg@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Unable to send message please try again later.')
            return render(request,'blog/post/thankYou.html')

    return render(request, "blog/post/contact1.html", {'form': form})



def post_detail(request, year, month, day, post,**kwargs):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request,'blog/post/detail.html',{'post': post})
