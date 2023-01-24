# 🧪 Sandbox 🧪

## 🎯 Objectives

> **Note**: Web content is contained and exposed via the folder [docs](docs).

Provide the following elements during online training web challenges/labs.

* A web server supporting HTTP and HTTPS protocols:
  * HTTPS via GitHub pages features.
  * HTTP via [THC disposable server](https://blog.thc.org/disposable-root-servers) instance.
* A network listener via a [THC disposable server](https://blog.thc.org/disposable-root-servers) instance.

## 🌎 URL

* GH pages url:
  * <https://righettod.github.io/sandbox/>
* GH pages deployment dashboard:
  * <https://github.com/righettod/sandbox/deployments>
  * <https://github.com/righettod/sandbox/deployments/activity_log?environment=github-pages>

## 💻 Misc commands

> **Note**: The exposed port is specified in the file `/config/self/reverse_port`.

On a [THC disposable server](https://blog.thc.org/disposable-root-servers) instance, use:
* `php -S 0.0.0.0:PORT` or `php -S 0.0.0.0:PORT -t docs` or use the script [start-webserver.sh](start-webserver.sh).
	* Start a PHP server.
* `git clone --depth 1 https://github.com/righettod/sandbox.git`
	* Clone the repository to use the sandbox anonymously.


