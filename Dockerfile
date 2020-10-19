FROM registry.redhat.io/ubi8/ubi-minimal:latest
COPY Pipfile Pipfile.lock /
RUN microdnf install python36 python3-pip && \
    pip-3 install --no-cache-dir pipenv && \
    pipenv lock --requirements > requirements.txt && \
    pip-3 install --no-cache-dir -r requirements.txt && \
    mkdir /app && \
    chmod g+rwX /app && \
    microdnf clean all
WORKDIR /app
COPY . /app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]