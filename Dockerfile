FROM alpine:3
RUN apk add --no-cache curl nmap bash 
RUN mkdir /righettod
RUN adduser -D -h /righettod -G root righettod
RUN chown -R righettod:root /righettod
USER righettod
RUN curl --output /righettod/kubectl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x /righettod/kubectl
RUN chmod -R 775 /righettod
WORKDIR /righettod
CMD ["/bin/bash"]
