# Каталог оборудования

## Локальный запуск

1. Установите зависимости командой `python -m pip install -r requirements.txt`.
2. Скопируйте `.env.example` в `.env` и задайте собственный `DJANGO_SECRET_KEY`.
   Сгенерировать его можно командой `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`.
3. Выполните `python manage.py migrate`.
4. При необходимости создайте локального администратора командой `python manage.py createsuperuser`.
5. Запустите сервер командой `python manage.py runserver`.
