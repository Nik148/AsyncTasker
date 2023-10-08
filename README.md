# AsyncTasker
Приложенин для запуска и мониторинга асинхронных задач

## Документация
Лучшая документация - это интерактивная документация). Поэтому после запуска приложения переходим по url: http://localhost:8000/docs

## Запуск
Docker:
```
docker-compose build
docker-compose up
```
## Мониторинг
### Grafana
Переходим по url: http://localhost:3000/
Нажимаем на кнопку "Toogle menu" и переходим в "Dashboards'
### Flower
Переходим по url: http://localhost:5555/
## Тестирование
```
pytest test
```
