from prometheus_client import start_http_server, Gauge
import time, random, os

PORT = int(os.getenv("PORT", "8000"))

# 10+ произвольных метрик (пример)
g_temp = Gauge("ext_temperature_c", "External temperature, C")
g_hum = Gauge("ext_humidity_pct", "External humidity, %")
g_wind = Gauge("ext_wind_mps", "Wind speed, m/s")
g_pressure = Gauge("ext_pressure_hpa", "Pressure, hPa")
g_cloud = Gauge("ext_cloud_pct", "Cloudiness, %")
g_uv = Gauge("ext_uv_index", "UV index")
g_pm25 = Gauge("ext_pm25", "PM2.5")
g_pm10 = Gauge("ext_pm10", "PM10")
g_pop = Gauge("ext_precip_prob", "Precip probability, %")
g_city_score = Gauge("ext_city_score", "Composite city score 0..100")

def fetch_stub_values():
    # Здесь можете подключить реальный API (OpenWeather и др.)
    # или оставить генератор — для проверки логики и визуализации.
    return {
        "t": random.uniform(-20, 40),
        "h": random.uniform(10, 95),
        "w": random.uniform(0, 20),
        "p": random.uniform(980, 1040),
        "c": random.uniform(0, 100),
        "uv": random.uniform(0, 11),
        "pm25": random.uniform(2, 150),
        "pm10": random.uniform(5, 200),
        "pop": random.uniform(0, 100),
    }

if __name__ == "__main__":
    start_http_server(PORT)
    while True:
        data = fetch_stub_values()
        g_temp.set(data["t"])
        g_hum.set(data["h"])
        g_wind.set(data["w"])
        g_pressure.set(data["p"])
        g_cloud.set(data["c"])
        g_uv.set(data["uv"])
        g_pm25.set(data["pm25"])
        g_pm10.set(data["pm10"])
        g_pop.set(data["pop"])
        # простая агрегированная метрика
        score = max(0, 100 - (data["pm25"] + data["pm10"])/5 - data["c"]/3 - data["pop"]/4)
        g_city_score.set(score)

        time.sleep(20)  # ~каждые 20 секунд по требованию
