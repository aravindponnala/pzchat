from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'index.html', {'test':'test'})


def room(request, room_name):
    print('hellooo')
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })
