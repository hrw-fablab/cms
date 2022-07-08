import json 

from .forms import ContactForm
from .models import Contact
from django.http import request, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == "POST":
        print("test")
        data = json.loads(request.body.decode('utf-8'))
        form = ContactForm(data)
        if form.is_valid():
            Contact.objects.get_or_create(email=form.cleaned_data["email"])
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})