from django.shortcuts import render
from .models import ProjectDetail, ClientFeedback, Contact
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
def index(requests):
    try:
        projects=ProjectDetail.objects.all()
        feedbacks=ClientFeedback.objects.all()

    except Exception as e:
        print("====models error====\t\t:",str(e))

    context={
        'projects':projects,
        'feedbacks':feedbacks,
    }
    return render(requests,'index.html',context)

def project_details(requests,project_id):

    return render(requests,'portfolio-details.html')
@csrf_protect
def contact_record(requests):
    if requests.method == "POST":
        name = requests.POST['name']
        email = requests.POST['email']
        subject = requests.POST['subject']
        message = requests.POST['message']
        contact= Contact.objects.create(name=name,email=email,subject=subject,message=message)
        contact.save()
    return JsonResponse("Congratulate your message sent Successfully.We will reach You within 1-hours",safe=False)
# Create your views here.
