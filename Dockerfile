# 1. Start with Python
FROM python:3.9-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy only the requirements file first
COPY requirements.txt .

# 4. Install the libraries from the list
RUN pip install -r requirements.txt

# 5. Now copy your app code
COPY app.py .

# 6. Run the app
CMD ["python", "app.py"]