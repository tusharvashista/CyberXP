from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    search_query = request.GET.get('q', '')
    try:
        # Get channel details
        channel_url = "https://www.youtube.com/@aakarshbonigala"
        
        # For now, we'll use the channel's uploads playlist
        # The search will be handled client-side by YouTube's player API
        context = {
            'search_query': search_query,
            'channel_url': channel_url,
            'channel_name': 'Aakarsh Bonigala',
            'channel_handle': '@aakarshbonigala'
        }
        return render(request, 'gallery.html', context)
    except Exception as e:
        print(f"Error in gallery view: {e}")
        context = {
            'search_query': search_query,
            'error': 'Unable to load videos. Please try again later.'
        }
        return render(request, 'gallery.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        messages.success(request, f'Thanks {name}! Your message has been received.')
        return redirect('contact')
        
    return render(request, 'contact.html')
