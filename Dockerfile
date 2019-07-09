FROM python:latest
RUN pip install requests
COPY get_slave_resources.py /
EXPOSE 8000
CMD python get_slave_resources.py && python -m http.server 8000
