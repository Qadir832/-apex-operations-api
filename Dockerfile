# 1. Base Image
FROM python:3.11-slim

# 2. Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Working Directory
WORKDIR /app

# 4. Dependencies copy aur install (Layer Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Non-Root User (security)
RUN useradd -m appuser

# 6. Baqi code copy 
COPY . .

# 7. Permissions 
RUN chown -R appuser:appuser /app

# 8. User switch 
USER appuser

# 9. Port expose
EXPOSE 8000

# 10. App start karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]