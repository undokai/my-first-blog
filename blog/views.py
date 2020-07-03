from django.shortcuts import render

def port_list(request):
    return render(request, 'blog/post_list.html', {})
