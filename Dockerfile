FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 设置启动脚本可执行权限
RUN chmod +x start.sh


EXPOSE 8080


CMD ["./start.sh"]