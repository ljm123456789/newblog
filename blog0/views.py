from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def index1(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:
        form = AddForm()
    return render(request, 'index2.html', {'form': form})


def post_comment(request, new_comment):
    if request.session.get('has_comment', False):
        return HttpResponse("you are already commented.")

'''
def login(request):
    m = Member.object.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id']  = m.id
        return HttpResponse('you are logged in. ')
    else:
        return HttpResponse('sorry')

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse('logged out')
'''

def index3(request):
    return render(request, 'blog/index3.html')

def columns(request):
    return render(request, 'blog/columns.html')