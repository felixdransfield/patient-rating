from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from userprofile.models import UserProfile
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def users(request):
    return render(request, 'users.html',
                  {'users': UserProfile.objects.all() })


@login_required
def edit_profile(request, user_id):
    a = request.user.id=user_id

    if request.method == "POST":
        f = UserProfileForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)

            c.user_id = a
            c.save()
            #takes user back to patient profile
            return HttpResponseRedirect('/accounts/profile/%s' % user_id)
    else:
        f = UserProfileForm()

    args = {}
    args.update(csrf(request))


    args['form'] = f

    return render(request, 'edit-profile.html', args)

@login_required
def user_profile(request, user_id):


    return render(request, 'profile.html',{'user_profile': UserProfile.objects.get(id=user_id),

                                         })
