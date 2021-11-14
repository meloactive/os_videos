from django.shortcuts import render, redirect

# Create your views here.
def demo_view(request):
    return render(request, 'os_videos_list/demo.html')