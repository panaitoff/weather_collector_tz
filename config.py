# config.py
DATABASE_URL = "sqlite:///weather_data.db"  # Используйте PostgreSQL, если нужно
API_URL = "https://api.open-meteo.com/v1/forecast"  # Замените на нужный API
API_PARAMS = {
    "latitude": 55.751244,  # Примерные координаты для Сколтеха
    "longitude": 37.618423,
    "current_weather": "true"
}
EXPORT_FILE = "weather_data.xlsx"
