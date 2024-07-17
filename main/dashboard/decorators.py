from django.shortcuts import redirect


def isOwner(model):
    def decorator(func):
        def wrapper(request, id, *args, **kwargs):
            if model.objects.get(id = id).author == request.user:
                return func(request, id, *args, **kwargs)
            else:
                return redirect('index')
        return wrapper
    return decorator
