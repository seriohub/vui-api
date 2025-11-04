FROM python:3.10-slim as velero-api-base
LABEL maintainer="DS"

# Update packages and install basics
RUN apt-get update && apt-get install --no-install-recommends -y \
	curl \
	python3-pip \
	git \
	restic \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

# prepare dir
RUN mkdir /app \
 && mkdir /app/data \
 && mkdir /app/velero-client \
# && mkdir /app/velero-client-binary
 && mkdir /app/data/seriohub/ \
 && mkdir /app/data/vmware-tanzu/

RUN curl -sL https://api.github.com/repos/seriohub/velero-ui/tags                       -o /app/data/seriohub/velero-ui-tags.json \
 && curl -sL https://api.github.com/repos/seriohub/velero-api/tags                      -o /app/data/seriohub/velero-api-tags.json \
 && curl -sL https://api.github.com/repos/vmware-tanzu/velero/tags                      -o /app/data/vmware-tanzu/velero-tags.json \
 && curl -sL https://api.github.com/repos/seriohub/velero-helm/tags                     -o /app/data/seriohub/velero-helm-tags.json \
 && curl -sL https://api.github.com/repos/seriohub/velero-watchdog/tags                 -o /app/data/seriohub/velero-watchdog-tags.json \
 && curl -sL https://api.github.com/repos/vmware-tanzu/velero/releases/latest           -o /app/data/vmware-tanzu/velero-releases-latest.json \
 && curl -sL https://raw.githubusercontent.com/seriohub/velero-helm/main/components.txt -o /app/data/components.txt

ADD https://github.com/vmware-tanzu/velero/releases/download/${VELERO_CLI_VERSION}/velero-${VELERO_CLI_VERSION}-linux-amd64.tar.gz	/app/velero-client/velero-${VELERO_CLI_VERSION}-linux-amd64.tar.gz
ADD https://github.com/vmware-tanzu/velero/releases/download/${VELERO_CLI_VERSION}/velero-${VELERO_CLI_VERSION}-linux-arm.tar.gz	/app/velero-client/velero-${VELERO_CLI_VERSION}-linux-arm.tar.gz
ADD https://github.com/vmware-tanzu/velero/releases/download/${VELERO_CLI_VERSION}/velero-${VELERO_CLI_VERSION}-linux-arm64.tar.gz	/app/velero-client/velero-${VELERO_CLI_VERSION}-linux-arm64.tar.gz


# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY ./src /app
# COPY ../velero-client /app/velero-client

# Exclude specific files or directories from the project
RUN find . -type f \( -name "*.yaml" -o -name "*.db" -o -name ".env" \) -delete \
 && find . -type d -name "__pycache__" -exec rm -rf {} + \
 && find . -type f -name "tmp" -delete

# install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin

# expose port
EXPOSE 8001

# Expose a volume the database
VOLUME /app/data

# Expose a volume for custom binary download
# VOLUME /app/velero-client-binary

WORKDIR /app/

RUN echo "Ready!"
CMD ["python3", "-u" , "__main__.py"]

# #####################################################################################################

FROM velero-api-base as velero-api
ARG VERSION
ARG BUILD_DATE

ENV BUILD_VERSION=$VERSION
ENV BUILD_DATE=$BUILD_DATE
