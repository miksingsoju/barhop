from django.shortcuts import render

# Create your views here.

def bar_list(request, username=None):
    return render(request, 'bars/bar-list.html')


def create_bar(request):
    ctx = {
        "stepper": [
            {
                "num": "1",
                "title": "Bar Details",
                "desc": "Set up your bar's details.",
                "current": "current",
            },
            {
                "num": "2",
                "title": "Add Events",
                "desc": "What's happening at your bar? Let people know!",
                "current": "",
            },
            {
                "num": "3",
                "title": "Add Tables",
                "desc": "Set up your bar's reservation system.",
                "current": "",
            },
            {
                "num": "4",
                "title": "Publish Your Bar",
                "desc": "Share your bar with the world!",
                "current": "",
            }
        ],
    }
    return render(request, 'bars/create-bar.html', ctx)


def bar_detail(request):
    return render(request, 'bars/bar-detail.html')