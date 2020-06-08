from django.shortcuts import render, redirect
from .models import Detail
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        designation = request.POST.get("designation", "")
        phone_number = request.POST.get("phone_number", "")
        email_id = request.POST.get("email", "")
        dob = request.POST.get("dob", "")
        portfolio_links = request.POST.get("portfolio_links", "")
        about_me = request.POST.get("about_me", "")
        objective = request.POST.get("objective", "")
        degree = request.POST.get("degree", "")
        field_degree = request.POST.get("field_degree", "")
        tenth_school = request.POST.get("tenth_school", "")
        tenth_board = request.POST.get("tenth_percentage", "")
        tenth_percentage = request.POST.get("tenth_percentage", "")
        twelfth_school = request.POST.get("twelfth_school", "")
        twelfth_board = request.POST.get("twelfth_board", "")
        twelfth_percentage = request.POST.get("twelfth_percentage", "")
        university = request.POST.get("university", "")
        avg_cgpa = request.POST.get("avg_cgpa", "")
        internship = request.POST.get("internship", "")
        work_experience = request.POST.get("work_experience", "")
        skills = request.POST.get("skills", "")

        profile = Detail(name=name,designation=designation,phone_number=phone_number,email_id=email_id,dob=dob,
                         portfolio_links=portfolio_links,about_me=about_me,objective=objective,
                         degree=degree,field_degree=field_degree,tenth_school=tenth_school,tenth_board=tenth_board,
                         tenth_percentage=tenth_percentage,twelfth_school=twelfth_school,twelfth_board=twelfth_board,
                         twelfth_percentage=twelfth_percentage,university=university,
                         avg_cgpa=avg_cgpa,internship=internship,work_experience=work_experience,skills=skills)

        profile.save()

    return render(request,'app/base.html')


def resume(request,id):
    user = Detail.objects.get(pk=id)
    template = loader.get_template('app/resume.html')
    html = template.render({'user':user})
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'

    return response




