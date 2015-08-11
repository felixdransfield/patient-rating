def user_context(request):

    group_id = request.user.groups.get().group_id

    return {
        'group_id': group_id
    }