from django.shortcuts import render, redirect
from .models import profile,Tweet
from .forms import TweetForm

# Create your views here.

def dashboard(request):
    form = TweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('twitter:dashboard')
    
    followed_tweets = Tweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")

    return render(request,"dashboard.html",{"form": form, "tweets": followed_tweets},)


def profile_list(request):
    profiles = profile.objects.exclude(user=request.user)
    return render(request, 'twitter/profile_list.html', {'profiles':profiles})

def Profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
        
    p = profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(p)
        elif action == "unfollow":
            current_user_profile.follows.remove(p)
        current_user_profile.save()
    return render(request, 'twitter/profile.html', {'profile':p})