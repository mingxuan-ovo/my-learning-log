#!/bin/bash

# 执行数据库迁移

echo "Applying database migrations..."
python manage.py migrate


# 启动Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8080 learning_log.wsgi:application