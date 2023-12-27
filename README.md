Все команды вводятся вне директории проекта:
mkdir project
скопируйте все файлы в папку project, но не переходите в неё

Установка необходимых пакетов:
pip install -r project/requirements.txt

Добавление базы данных:
mysql
create user 'user'@'localhost' identified by 'password';
grant all privileges on * . * to 'user'@'localhost';
create database memes;
exit;
// Таблицы создадутся автоматически внутри __init__.py

Запуск проекта:
export FLASK_APP=project
export FLASK_DEBUG=1 // Необязательно, необходимо для отслеживания ошибок
flask run // Может потребоваться ключ --host="0.0.0.0"

Для перехода на страницы приложения писать в адресной строке браузера: localhost:5000