from django.shortcuts import render
from .sentiment import analyze_sentiment
from .models import SentimentHistory

def home(request):

    result = ""

    text = ""

    if request.method == "POST":

        text = request.POST.get('text')

        result = analyze_sentiment(text)

        SentimentHistory.objects.create(
            text=text,
            result=result
        )

    history = SentimentHistory.objects.all().order_by('-created_at')

    return render(
        request,
        'home.html',
        {
            'result': result,
            'text': text,
            'history': history
        }
    )
