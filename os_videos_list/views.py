from django.shortcuts import render, redirect

# Create your views here.
def demo_view(request):
    test_arr = []
    for i in range(10):
        test_arr.append(i)
    return render(request, 'os_videos_list/demo.html', {"lists": test_arr})