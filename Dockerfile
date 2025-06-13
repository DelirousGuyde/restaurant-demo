# ---------- base image ----------
    FROM python:3.11-slim

    # ---------- env & workdir ----------
    ENV PIPENV_VENV_IN_PROJECT=1 \
        PYTHONUNBUFFERED=1
    WORKDIR /app
    
    # ---------- system packages ----------
    RUN apt-get update -qq && \
        apt-get install --no-install-recommends -y build-essential && \
        rm -rf /var/lib/apt/lists/*
    
    # ---------- dependency installation ----------
    # Copy only the lockfiles first so Docker cache survives code changes
    COPY Pipfile* ./
    RUN pip install --no-cache-dir pipenv && \
        pipenv install --deploy --system --ignore-pipfile
    
    # ---------- application source ----------
    COPY . .
    
    # ---------- runtime ----------
    EXPOSE 5000
    CMD ["python", "restaurant_demo.py"]