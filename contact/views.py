"""
==============================================================================
CONTACT VIEWS
Renders contact form & FAQ accordion page.
==============================================================================
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FAQItem
from .forms import ContactForm

def contact_view(request):
    """Contact page with message form and FAQs."""
    faqs = FAQItem.objects.filter(is_featured=True)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact:index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form, 'faqs': faqs})

def faq_view(request):
    """Dedicated FAQ list."""
    faqs = FAQItem.objects.all()
    return render(request, 'contact/faq.html', {'faqs': faqs})
