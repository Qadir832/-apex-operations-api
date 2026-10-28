from fastapi import FastAPI, HTTPException
import psycopg2
import os
import logging
import json

# 1. Structured Logging Setup (JSON format)
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

# 2. Health Endpoint (Liveness)
@app.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "healthy"}

# 3. Readiness Endpoint (Database check)
@app.get("/ready")
def readiness_check():
    logger.info("Readiness check endpoint hit")
    try:
        # Database URL environment variable se aa raha hai (Security)
        db_url = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/apexdb")
        conn = psycopg2.connect(db_url, connect_timeout=2)
        conn.close()
        return {"status": "ready", "database": "connected"}
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Database not ready")