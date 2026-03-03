FROM alpine:3
RUN apk add --no-cache curl wget ca-certificates bash zsh git nano vim tmux nmap nmap-scripts whois ttyd grep httpie netcat-openbsd py3-setuptools py3-virtualenv python3 python3-dev py3-pip
RUN mkdir /righettod
RUN adduser -D -h /righettod -G root righettod
RUN chown -R righettod:root /righettod
USER righettod
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
RUN find /usr/share/nano/ -iname "*.nanorc" -exec echo include {} \; >> /righettod/.nanorc
RUN touch /righettod/.hushlogin
RUN echo "set -g mouse on" > /righettod/.tmux.conf
RUN chmod -R 775 /righettod
RUN chmod -R 755 /righettod/.oh-my-zsh
CMD ["/bin/zsh"]
