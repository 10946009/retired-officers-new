# 使用Python官方镜像作为基础镜像
FROM python:3.12-bullseye

# 更新apt源并安装依赖
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

# 安装Poetry
RUN curl -sSL https://install.python-poetry.org | python3

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件（除了.dockerignore排除的路径）都拷贝进入镜像的/app目录
COPY . /app

# 安装Python依赖
RUN pip install poetry
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install

# 指定容器启动时运行Python应用
# CMD ["python3", "manage.py","0.0.0.0:8080"]