FROM alpine:3.19
RUN apk add --no-cache curl wget ca-certificates bash zsh git nano vim
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
CMD ["/bin/zsh"]
