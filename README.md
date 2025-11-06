# 🌐 Monitoring Assignment 4 — Prometheus & Grafana Dashboards

![Grafana Banner](https://github.com/grafana/grafana/raw/main/public/img/grafana_icon.svg)


## 🧭 Overview
This project implements a **complete monitoring system** built on **Prometheus** and **Grafana**, featuring three interconnected exporters:

| Exporter Type | Description | Tool / Source |
|----------------|--------------|----------------|
| 🐘 **Database Exporter** | Tracks PostgreSQL performance (queries, cache, TPS) | `prometheuscommunity/postgres-exporter` |
| 💻 **Node Exporter** | Monitors CPU, RAM, Disk, and Network usage | `prom/node-exporter` |
| 🌤 **Custom Exporter** | Collects live metrics from external APIs | Custom `Python Exporter` |

Together, they provide real-time insights into database health, system performance, and external data — all visualized through interactive Grafana dashboards with automated Telegram alerts.

---

## 🧱 Project Structure
```

MONITORING-ASSIGNMENT4/
│
├── custom_exporter.py          # Python exporter for external APIs
├── docker-compose.yml              # Main stack (Prometheus, Grafana, Exporters)
├── Dockerfile.custom               # Build file for custom exporter
├── prometheus.yml                  # Prometheus configuration
├── postgres_load_test.sql          # SQL script to simulate database activity
└── README.md                       # Project documentation

```

## ⚙️ Setup Instructions

### 🐳 1. Start the Monitoring Stack
From your project root:
```bash
docker-compose up -d
````

Services launched:

* **Prometheus** — collects metrics
* **Grafana** — visualization
* **PostgreSQL** — test database
* **pg_exporter** — PostgreSQL metrics
* **node_exporter** — system metrics
* **custom_exporter** — external API metrics

### 🔗 2. Access Interfaces

| Service             | URL                                            | Default Login   |
| ------------------- | ---------------------------------------------- | --------------- |
| Grafana             | [http://localhost:3000](http://localhost:3000) | `admin / admin` |
| Prometheus          | [http://localhost:9090](http://localhost:9090) | —               |
| PostgreSQL Exporter | [http://localhost:9187](http://localhost:9187) | —               |
| Node Exporter       | [http://localhost:9100](http://localhost:9100) | —               |
| Custom Exporter     | [http://localhost:8000](http://localhost:8000) | —               |


---

## 💾 Database Load Simulation

To generate live metric activity on the PostgreSQL dashboard:

```bash
docker cp .\postgres_load_test.sql postgres:/tmp/postgres_load_test.sql
docker exec -it postgres psql -U postgres -d postgres -f /tmp/postgres_load_test.sql
```

This script continuously performs:

* **INSERT**, **UPDATE**, and **DELETE** operations
* Generates fluctuating values for TPS, Buffers, Tuples, and Cache metrics

---

## 📊 Dashboards Overview

### 🐘 PostgreSQL — Database Dashboard

**Purpose:** Monitor internal database health and performance.

**Main Panels:**

* Active / Idle Connections
* Transactions Per Second (TPS)
* Database Size (GB)
* Cache Hit Ratio (%)
* Blocks Read / Hit per second
* Live & Dead Tuples
* Checkpoints & Buffers Allocated

**Alert:**
🚨 *Cache Hit Ratio Below 90%*
🚨 *High Connections Usage above 70%*
→ Sends Telegram alert if DB caching efficiency drops or Connections Usage increases.

---

### 💻 Node — System Metrics

**Purpose:** Visualize system-level resource usage and machine health.

**Main Panels:**

* CPU Usage (%) and Load Average (1m)
* RAM & Swap Usage (%)
* CPU per Core (%) and IOwait (%)
* Disk Read / Write (B/s)
* Free Disk Space (GB)
* Network In / Out (Mbit/s)
* Network Errors (1/s)

These metrics reflect overall system stability and load distribution.

**Alert:**
🚨 *High Memory Usage above 85%*
→ Sends Telegram alert if Memory Usage increases too much.

---

### 🌤 Custom — External API Metrics

**Purpose:** Display real-time environmental or API-based metrics collected via a Python exporter.

**Main Panels:**

* Temperature (°C), Humidity (%), Pressure (hPa)
* Wind Speed (m/s), Cloudiness (%), Precipitation Probability (%)
* PM2.5 / PM10 (µg/m³) — Air Quality
* Composite City Score (aggregated health metric)
* Average Temperature (5m) & Score Volatility (10m Stddev)

**Alert:**
🚨 *Composite City Score*
→ Telegram alert when environmental index fluctuates beyond thresholds.

---

## 🛰 Alerting Integration (Telegram)

Grafana alerts are connected through **Telegram Bot API**.
When a condition is triggered (e.g., CPU > 85%, Cache Ratio < 90%),
a notification is sent to the configured chat.

**Example message:**

```
🚨 Grafana Alert
Alert: Composite City Score
Status: firing
Instance: custom_exporter:8000
```

---

## 🧪 Load Simulation Summary

* **PostgreSQL:** Automated SQL script (`postgres_load_test.sql`) generating active inserts/updates/deletes.
* **Node Exporter:** Reflects live CPU, RAM, and I/O usage from Docker host.
* **Custom Exporter:** Updates external API values (e.g., temperature, air quality) every ~20 seconds.

This ensures all dashboards display real-time data even during demonstrations.

---

## 🏁 Conclusion

This project demonstrates an end-to-end monitoring solution integrating **system, database, and external data sources** into a unified Grafana environment.
It showcases:

* Real-time metric collection
* Intelligent visualization and alerting
* Practical DevOps monitoring setup using Docker
