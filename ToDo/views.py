from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, CategoryForm
from .models import Task


def start(request):
    """
    Главная страница
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: бъект HttpResponse, содержащий ответ
    """
    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, отображаем шаблон 'home.html'
        return render(request, 'home.html', {})
    else:
        # Если пользователь не аутентифицирован, отображаем шаблон 'no_log.html'
        return render(request, 'no_log.html', {})


def all_users(request):
    """
    Get all users
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    # Получение всех пользователей из базы данных
    users = User.objects.all()
    context = {
        'users': users,
    }

    # Отображение шаблона 'listusers.html' с контекстом
    return render(request, "listusers.html", context)


def pers_user(request, user_id):
    """
    Get user by ID
    :param request: объект HttpRequest, содержащий информацию о запросе
    :param user_id: ID пользователя
    :return: объект HttpResponse, содержащий ответ
    """
    # Получение пользователя по указанному ID или возврат ошибки
    # 404, если пользователь не найден
    user = get_object_or_404(User, id=user_id)
    # Создание контекста для передачи данных в шаблон
    context = {
        'user': user,
    }

    # Отображение шаблона 'pers_user.html' с контекстом
    return render(request, "pers_user.html", context)


def create_task(request):
    """
    Create Task
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    if request.method == "POST":
        # Если метод запроса POST, создаем экземпляр формы с данными из запроса
        form = TaskForm(request.POST)
        if form.is_valid():
            # Если форма действительна, сохраняем данные формы
            form.save()
            # Перенаправляем пользователя на главную страницу
            return redirect('/')
    else:
        # Если метод запроса GET, создаем пустой экземпляр формы
        form = TaskForm()
    # Создание контекста для передачи данных в шаблон
    context = {
        'form': form
    }

    # Отображение шаблона 'create_task.html' с контекстом
    return render(request, 'create_task.html', context)


def create_category(request):
    """
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    if request.method == "POST":
        # Если метод запроса POST, создаем экземпляр формы с данными из запроса
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Если форма действительна, сохраняем данные формы
            form.save()
            # Перенаправляем пользователя на главную страницу
            return redirect('/')
    else:
        # Если метод запроса GET, создаем пустой экземпляр формы
        form = CategoryForm()
        # Создание контекста для передачи данных в шаблон
        context = {

            'form': form
        }
    # Отображение шаблона 'create_category.html' с контекстом
    return render(request, "create_category.html", context)


def get_task_user(request):
    """
    Get all tasks for user (GET)
    Получить все задачи для пользователя
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    # Получение ID пользователя из запроса
    user_id = request.user.id
    # Получение всех задач, созданных данным пользователем
    task = Task.objects.filter(created_by=user_id)
    # Вывод ID пользователя и его имени в консоль (для отладки)
    print(user_id, request.user.username)
    # Создание контекста для передачи данных в шаблон
    context = {
        'task': task,
    }
    # Отображение шаблона 'get_task_user.html' с контекстом
    return render(request, "get_task_user.html", context)


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def user_detail(request):
    """
    Вывод пользователя по ID.

    :param request: объект запроса
    :return: ответ с отображением шаблона 'user_detail.html'
    """
    user = None  # Инициализируем переменную user значением None

    if request.method == 'POST':  # Проверяем, был ли запрос методом POST
        id = request.POST.get('user_id')  # Получаем значение 'user_id' из POST-запроса
        try:
            user = User.objects.get(id=id)  # Пытаемся найти пользователя по указанному идентификатору
        except User.DoesNotExist:
            user = None  # Если пользователь не найден, устанавливаем user в значение None

    return render(request, 'user_detail.html', {'user': user})
    # Возвращаем ответ, отображая шаблон 'user_detail.html' и передавая переменную user в контексте шаблона


def task(request):
    """
    Отображает список задач пользователя.

    :param request: Запрос от клиента.
    :return: Отрендеренный шаблон с списком задач.
    """
    user = request.user
    tasks = Task.objects.filter(created_by=user)
    return render(request, 'task.html', {'tasks': tasks})
