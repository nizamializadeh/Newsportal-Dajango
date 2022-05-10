from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    login_url = []
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
            print("+_+_+_+_+_+")
            login_url.append(u.groups.all()[0].name)
        return False
     
    return user_passes_test(in_groups)