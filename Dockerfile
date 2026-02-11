# Base image (Python already installed)
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# First train model, then run app
CMD python model.py && python app.py
