FROM python:3.9
WORKDIR /usr/tools/autoFindPositionByBoss
ENV TZ Asia/Shanghai
COPY . /usr/tools/autoFindPositionByBoss
RUN echo "安装项目依赖"
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD python runner.py



