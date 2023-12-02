from django.shortcuts import render
import datetime


def home(request):
    # Additional data for the template
    d = {
        "author": "Rahim",
        "age": 5,
        "lst": ["python", "is", "best"],
        "birthday": datetime.datetime.now(),
        "val": "",
        "courses": [
            {"id": 1, "name": "Python", "fee": 5000},
            {"id": 2, "name": "Django", "fee": 10000},
            {"id": 3, "name": "C", "fee": 1000},
        ],
        # Additional data starts here
        "additional_info": {
            "city": "Example City",
            "country": "Example Country",
            "website": "https://www.example.com",
            "tags": ["programming", "web development", "django"],
            "description": "This is an example description.",
        },
        "additional_info1": [
            {"city": "Example City", "country": "Example Country"},
            {"city": "Another City", "country": "Another Country"},
            # ... other dictionaries
        ],
    }
    return render(request, "home.html", d)
