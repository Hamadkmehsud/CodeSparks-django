from django.shortcuts import render, redirect
from .models import UserInfoModel , UserRegisterModel
from .userform import CreateUserForm




def login(request):
    return render(request, 'userprofile/login.html')

# Create your views here.
def create_profile(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            image = form.cleaned_data['image']
            # Create user and profile instances
            user = UserRegisterModel(username=username)
            user.set_password(password)  # Hash the password
            user.save()
            # Create user profile
            profile = UserInfoModel(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                image=image
            )
            profile.save()

            return redirect('some-success-url')  # Redirect to a success page or profile page
    else:
        form = CreateUserForm()

    return render(request, 'userprofile/create-profile.html', {'form': form})

    # return render(request, "userprofile/create-profile.html")