# Weather Data Collector

Проект для сбора данных о погоде через API и их сохранения в базе данных с дальнейшей возможностью экспорта в Excel файл. Данные собираются асинхронно каждые 3 минуты и включают: температуру, скорость и направление ветра, давление, тип и количество осадков.

## Используемые технологии
- Python 3
- SQLAlchemy (ORM для работы с базой данных)
- Aiohttp (асинхронные HTTP-запросы)
- Pandas (для экспорта данных в Excel)
- SQLite (по умолчанию в качестве базы данных)
- Open-Meteo API (или другое API для получения данных о погоде)

## Установка и настройка

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/yourusername/weather-data-collector.git
    cd weather-data-collector
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
    ```

3. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте конфигурацию API и базы данных:**
    В файле `config.py` укажите API для получения данных о погоде, например, Open-Meteo:
    ```python
    DATABASE_URL = "sqlite:///weather_data.db"  # По умолчанию используется SQLite
    API_URL = "https://api.open-meteo.com/v1/forecast"  # Open-Meteo API
    API_PARAMS = {
        "latitude": 55.751244,  # Примерные координаты Сколтеха
        "longitude": 37.618423,
        "current_weather": "true"
    }
    EXPORT_FILE = "weather_data.xlsx"
    ```

## Запуск

### Сбор данных о погоде:
Для запуска скрипта сбора данных используйте команду:
```bash
python weather_data_collector.py
