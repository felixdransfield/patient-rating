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
    if request.method == "POST":
        f = UserProfileForm(request.POST, instance=request.user.profile)
        if f.is_valid():
            f.save()

            return HttpResponseRedirect('/accounts/profile/%s' % user_id)
    else:
        user = request.user
        profile = user.profile
        f = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))


    args['form'] = f

    return render(request, 'edit-profile.html', args)

@login_required
def user_profile(request, user_id):
    a = UserProfile.objects.filter(user__id=user_id)


    if a.exists():
        return render(request, 'profile.html',{'user_profile': UserProfile.objects.get(user__id=user_id),



                                         })
    else:
        return HttpResponseRedirect('/accounts/profile/edit/%s' % user_id)