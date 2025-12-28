from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    return HttpResponse("hello")

def index(request):
    if "email_id" in request.session or "user_name" in request.session:
        c_id=Category.objects.all()
        register_user=Register.objects.get(email_id=request.session['email_id'])
        expense_id=Add_Expense.objects.filter(register_user=register_user)
        print(expense_id)
        salary=register_user.salary
        total_expense=0
    
        for i in expense_id:
            total_expense=total_expense+i.amount

        disposable_amount=salary-total_expense
        context={'c_id':c_id,'expense_id':expense_id,'total_expense':total_expense,'salary':salary,'disposable_amount':disposable_amount}
        return render(request,'index.html',context)
    else:
        return render(request,'login.html')

def add_expense(request):
    if "email_id" in request.session or "user_name" in request.session:
        if request.POST:
            register_user=Register.objects.get(email_id=request.session['email_id'])
            title=request.POST.get('title').strip()
            amount=request.POST.get('amount').strip()
            category=request.POST.get('category').strip()
            print("hello")
            Add_Expense.objects.create(register_user=register_user,title=title,amount=amount,category=category)
            return redirect('index')
        else:
            return render(request,'login.html')
   

def edit(request):
    if "email_id" in request.session or "user_name" in request.session:
        c_id=Category.objects.all()
        edit_expense_id=request.GET.get('expense_id')
        edit_expense=Add_Expense.objects.get(id=edit_expense_id)
        print("hello",edit_expense.category)
        context={'c_id':c_id,'edit_expense_id':edit_expense_id,'edit_expense':edit_expense,'category':edit_expense.category}
        return render(request,'edit_expense.html',context) 
    else:
        return render(request,'login.html')

def delete(request):
    if "email_id" in request.session or "user_name" in request.session:
        if request.POST:
            edit_expense_id=request.GET.get('expense_id')
            edit_expense=Add_Expense.objects.get(id=edit_expense_id)
            edit_expense.delete()
            return redirect('index')
    else:
        return render(request,'login.html')


def edit_expense(request):
    if "email_id" in request.session or "user_name" in request.session:
        if request.POST:
            c_id=Category.objects.all()
            edit_expense_id=request.GET.get('expense_id')
            edit_expense=Add_Expense.objects.get(id=edit_expense_id)
            title=request.POST.get('title').strip()
            amount=request.POST.get('amount').strip()
            category=request.POST.get('category').strip()
            if not all([title,amount,category]):
                return render(request, 'edit_expense.html', {'alert': 'Please fill all fields.', "c_id": c_id,})
            edit_expense.title=title
            edit_expense.amount=amount
            edit_expense.category=category
            edit_expense.save()
            context={'c_id':Category.objects.all(),
            'expense_id':Add_Expense.objects.all()}
            return render(request,'index.html',context)
        context={'c_id':Category.objects.all(),
        'expense_id':Add_Expense.objects.all()}
        return render(request,'edit_expense.html',context) 
    else:
        return render(request,'login.html')

def edit_salary(request):
    if "email_id" in request.session or "user_name" in request.session:
        if request.POST:
            salary = request.POST.get('salary', '').strip()
            register_user=Register.objects.get(email_id=request.session['email_id'])
            register_user.salary=salary
            register_user.save()
            return redirect('index')
    else:
        return render(request,'login.html')



def login(request):
    if request.method == "POST":
        email_id = request.POST.get('email_id', '').strip()
        password = request.POST.get('password', '')
        if not email_id or not password:
            return render(request, 'login.html', {'alert': 'Please enter both email and password.'})
        user_qs = Register.objects.filter(email_id=email_id)
        if not user_qs.exists():
            return render(request, 'login.html', {'alert': 'Email not registered.'})
        user = user_qs.first()
        if password == user.password:
            request.session['email_id'] = email_id
            request.session['user_name'] = user.full_name
            return redirect('index')
        return render(request, 'login.html', {'alert': 'Invalid Password.'})
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', '').strip()
        email_id = request.POST.get('email_id', '').strip()
        phone_no = request.POST.get('phone_no', '').strip()
        salary = request.POST.get('salary', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        if not all([full_name, email_id, phone_no, password, confirm_password,salary]):
            return render(request, 'register.html', {'alert': 'Please fill all fields.'})
        if password != confirm_password:
            return render(request, 'register.html', {'alert': 'Passwords do not match.'})
        Register.objects.create(full_name=full_name, email_id=email_id, phone_no=phone_no,salary=salary, password=password, confirm_password=confirm_password)
        request.session['email_id'] = email_id
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    # remove only auth/session keys so messages framework keeps working normally
    request.session.pop('email_id', None)
    request.session.pop('user_name', None)
    messages.success(request, "Logged out successfully!")
    return redirect('login')