def base_context(request):
    can_see_dashboard = False
    if request.user.is_authenticated:
        can_see_dashboard = (
            request.user.is_superuser or
            request.user.groups.filter(name__in=['Manager', 'Editor']).exists()
        )

    return {
        'can_see_dashboard': can_see_dashboard
    }

def see_admin_or_manager(request):
    can_see_users = False
    if request.user.is_authenticated:
        can_see_users = (
            request.user.is_superuser or
            request.user.groups.filter(name__in=['Manager']).exists()
        )

    return {
        'can_see_users': can_see_users
    }
