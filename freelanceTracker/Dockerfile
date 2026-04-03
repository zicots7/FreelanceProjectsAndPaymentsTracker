FROM python:3.13.5-alpine

# 2. Set the WORKDIR to the home directory 
WORKDIR /home/app/freelanceTracker

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy files 
COPY . .

#Exposing the app to port 
EXPOSE 8081
# 5. Use a port (e.g., 8081)
CMD ["gunicorn", "-b", "0.0.0.0:8081", "freelanceTracker.wsgi:application"]