from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from userprofile.models import UserProfile
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request, user_id):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form


    return render(request, 'edit-profile.html', args)

@login_required
def user_profile(request, user_id):

    return render(request, 'profile.html',{'user_profile': UserProfile.objects.get(id=user_id),
                                         })
