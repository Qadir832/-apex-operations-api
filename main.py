import json
import logging
import os

import psycopg2
from fastapi import FastAPI, HTTPException
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

# Custom JSON Logger setup
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)

logger = logging.getLogger("apex-api")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

app = FastAPI(title="Apex Operations API")

@app.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "healthy"}

@app.get("/ready")
def readiness_check():
    logger.info("Readiness check endpoint hit")
    try:
        db_url = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/apexdb")
        conn = psycopg2.connect(db_url, connect_timeout=2)
        conn.close()
        return {"status": "ready", "database": "connected"}
    except psycopg2.Error as e:
        logger.error(f"Database connection failed: {e!s}")
        raise HTTPException(status_code=503, detail="Database not ready")

# ==========================================
# YEH NAYA ENDPOINT ADD HUA HAI (METRICS)
# ==========================================
@app.get("/metrics")
def metrics():
    logger.info("Metrics endpoint hit")
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)