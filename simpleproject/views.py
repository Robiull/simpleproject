from django.shortcuts import render, HttpResponse
def home(request):
    if request.method=="POST":
        name=["nidhi","robiul","sohag","fatemee"]
    else:
        name=["robiul","fatemee","nidhi","sohag"]
    context={
        'name':name,
    }
    return render(request,'home.html',context)

def Contact(request):
    if request.method=="POST":
        name=request.POST['savename']
        phone=request.POST['savephone']
        content=request.POST['savecontent']
        print(name)
        print(phone)
        print(content)
    return render(request,'Contact.html')