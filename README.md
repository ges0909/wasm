# Webassembly (Wasm)

## Motivation

> _Ich prophezeie, dass WebAssembly die heutige Front-End-Entwicklung irgendwann überholen wird und eine ganz neue Welt entstehen wird._
> 
> -- Matt Wattson, [20 Jahre Arbeit und nichts als technische Schulden](https://www.golem.de/news/technical-debt-40-jahre-arbeit-und-nichts-als-technische-schulden-2306-175091.html)

## Links

- [https://www.fermyon.com/blog/introducing-spin-v1](https://www.fermyon.com/blog/introducing-spin-v1)
- [WebAssembly (Wasm): Past, Present, Future | Eröffnungs-Keynote BASTA! Spring 2023 in Frankfurt](https://yewtu.be/watch?v=0Bh_YcUWsiM)
- [Writing Server Side WebAssembly with Python | Complete Guide to Spin](https://yewtu.be/watch?v=neAnYfIcNLE)
- [https://wasmlabs.dev/articles/docker-without-containers/](https://wasmlabs.dev/articles/docker-without-containers/)

## Wasm

---

- Virtual **binary** instruction format, compiled from different source languages
- **Web** = supported by all major browsers, **Assembly** seems to be something like the good-old assembler

---

- **Resource utilization**, With same compute power, more applications could be executed
- **Speed**, Wasm modules are bootstrapped in no-time and fast at runtime
- **Security**, Wasm modules are isolated (sandbox) and have dedicated permissions
- **Size**, Wasm is tiny compared to containers or VMs

---

- **WASI**, WebAssembly System Interface, Spec only
- **Platform-agnostic**, Wasm application could run on any WASI-compliant platform
- Designed to provide only essential system calls to Wasm modules

---

- Wasi runtime, Delegates system calls to system, Thin layer

---

- Serverless, No infrastructure management
- Wasm speed allows scale-down to 0
- Low impact on request performance

---

- Spin: Runtime, SDK, Developer Tooling
- `spin.toml`, Spin app Manifest

---

## Serverless

- Serverless = Function as a Service (FaaS)

---

- AWS Lambda
- Azure Functions
- Google Cloud Functions

## Spin 

Download and Install Spin.

1. [Download](https://github.com/fermyon/spin/releases/download/v1.3.0/spin-v1.3.0-windows-amd64.zip)
1. [Install](https://developer.fermyon.com/spin/quickstart#install-spin)


Show installed templates.

```shell
spin template list
```

```shell
spin plugins update
```

Install Python plugin to compile Python module with all its dependencies to produce
Spin-compatible WebAssembly module.


```shell
spin plugin install py2wasm --yes
```

Install "Python HTTP Request Handler" Template.


```shell
spin templates install --git https://github.com/fermyon/spin-python-sdk --update
```

```shell
spin plugin install cloud --yes
```

Create Application.


```shell
spin new [ --accept-defaults ] http-py hello
tree
```

Build Application.


```shell
cd wasm-py-demo
spin build
```

Run Application.


```shell
spin up
```

Login to Fermyon.


```shell
spin login
```

Deploy to Fermyon Cloud.


```shell
spin deploy
```

## Install load tester Hey

- download [here](https://hey-release.s3.us-east-2.amazonaws.com/hey_windows_amd64)
- rename to `hey.exe`
- add path to `PATH`.
