from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")

        UserDetails.objects.create(username=username, email=email, password=password)
        return redirect('login')  # ✅ redirect to login after successful signup

    return render(request, 'loginify/signup.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                # Login success
                return render(request, 'loginify/success.html', {'user': user})
            else:
                # Password incorrect
                return render(request, 'loginify/login.html', {'error': 'Invalid password'})
        except UserDetails.DoesNotExist:
            # User with email does not exist
            return render(request, 'loginify/login.html', {'error': 'User not found'})

    # If GET request, just render the login form
    return render(request, 'loginify/login.html')


def logout_view(request):
    # No session management is done here since we’re not using Django’s auth
    return redirect('login')


def success_view(request):
    return render(request, 'loginify/success.html')

def get_all_users(request):
    users = UserDetails.objects.all().values()
    return JsonResponse(list(users), safe=False)


def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user_data = {
            'username': user.username,
            'email': user.email,
            'password': user.password,
        }
        return JsonResponse(user_data)
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)


@csrf_exempt
def update_user(request, email):
    if request.method == 'PUT':
        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        try:
            data = json.loads(request.body)

            # Check if email is being updated and if it exists for a different user
            new_email = data.get('email', user.email)
            if new_email != user.email:
                if UserDetails.objects.filter(email=new_email).exclude(pk=user.pk).exists():
                    return JsonResponse({'error': 'Email already in use'}, status=400)
                user.email = new_email

            # Update other fields
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)

            user.save()

            return JsonResponse({'message': 'User updated successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        try:
            user = UserDetails.objects.get(Email=email)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"})
        except UserDetails.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"error": "Only DELETE method allowed"}, status=405)
