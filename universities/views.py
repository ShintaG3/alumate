from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import json

from my_universities.models import MyUniversity
from my_profiles.models import MyProfile
from django.contrib.auth.models import User
from boards.models import Post

f = open('static/json/uni_js.json','r')
ud = json.load(f)

@login_required
def University(request):
    user = request.user
    id = request.user.id
    myuni = user.university.all().first()
    uni_name = myuni.uni_name
    if not uni_name:
        return redirect('my_university')

    # uni_pk = MyUniversity.objects.get(pk=id)
    # myuniversity = uni_pk.uni_name

    for i in ud:
        u = i.get(uni_name,None)
        if u:
            uni_image = u.get("image",None)
            country = u.get("country",None)
            break
        else:
            uni_image = None
            country = None
            pass

    qs_apl = MyUniversity.objects.filter(uni_name=uni_name, enr_status="applicant")
    qs_crt = MyUniversity.objects.filter(uni_name=uni_name, enr_status="current student")
    qs_alm = MyUniversity.objects.filter(uni_name=uni_name, enr_status="alumni")
    apl_count = qs_apl.count()
    crt_count = qs_crt.count()
    alm_count = qs_alm.count()
    posts = Post.objects.all()

    context = {
        'uni_name':uni_name,
        'country':country,
        'uni_image':uni_image,
        # 'pro_image':pro_image,
        # 'introduction':introduction,
        'qs_apl':qs_apl,
        'qs_crt':qs_crt,
        'qs_alm':qs_alm,
        'apl_count':apl_count,
        'crt_count':crt_count,
        'alm_count':alm_count,
        'posts':posts,
    }
    return render(request, 'universities/university.html', context)
