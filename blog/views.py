from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from .forms import MyForm
from django.views.generic.edit import FormView

def index(request):
    return render(request, "blog/index.html")
def blog_visit(request):
    return render(request, 'blog/blog_page.html')

def about_page_redirect(request):
    return render(request, 'blog/about_page.html')

def feedback(request):
    return render(request, 'blog/feedback.html')



class ContactFormView(FormView):
    form_class = MyForm
    template_name = 'feedback.html'
    success_url = '/success/'  # Replace with your desired success URL name

    def form_valid(self, form):
        # Process the form data
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']
        # You can add any additional processing here
        print(form.cleaned_data)
        # Save the form data or perform other actions
        # ...
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()  # Include the form in the context
        return context

    



def get_name(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            # Process the data
            # Redirect or render a success page
        else:
            return render(request, 'feedback.html', {'form': form})
    else:
        form = MyForm()

    return render(request, 'feedback.html', {'form': form})


# def form_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']

#         else:
#             pass

#     else:
#         form = MyForm()

    
#     return render(request, 'blog_page.html', {'form': form, 'name': name, 'email': email})

        

# class ContactformView(request):
#     template_name = "feedback.html"
#     form_class = MyForm
#     success_url = "'/thanks"
