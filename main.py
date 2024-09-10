# weather_data_collector.py
import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
from sqlalchemy.orm import Session
from models import WeatherData, SessionLocal
import config

async def fetch_weather(session):
    async with session.get(config.API_URL, params=config.API_PARAMS) as response:
        return await response.json()

async def save_weather_data(data):
    db = SessionLocal()
    weather_data = WeatherData(
        date=datetime.now().strftime("%H:%M:%S %D"),
        temperature=data['current_weather']['temperature'],
        wind_speed=data['current_weather']['windspeed'],
        wind_direction=data['current_weather']['winddirection'],
    )
    db.add(weather_data)
    db.commit()
    db.close()

async def export_to_excel():
    db = SessionLocal()
    data = db.query(WeatherData).order_by(WeatherData.date.desc()).limit(10).all()
    df = pd.DataFrame([{
        'date': wd.date,
        'Temperature': wd.temperature,
        'Wind Speed': wd.wind_speed,
        'Wind Direction': wd.wind_direction,
    } for wd in data])
    df.to_excel(config.EXPORT_FILE, index=False)
    db.close()

async def main():
    while True:
        async with aiohttp.ClientSession() as session:
            data = await fetch_weather(session)
            await save_weather_data(data)

        await export_to_excel()
        await asyncio.sleep(180)  # Запрашиваем каждые 3 минуты

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
