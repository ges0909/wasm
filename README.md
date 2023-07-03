# Webassembly (Wasm)

## Motivation

> Ich prophezeie, dass WebAssembly die heutige Front-End-Entwicklung irgendwann überholen wird und eine ganz neue Welt entstehen wird.

aus: [20 Jahre Arbeit und nichts als technische Schulden](https://www.golem.de/news/technical-debt-40-jahre-arbeit-und-nichts-als-technische-schulden-2306-175091.html)

## Links

- [https://www.fermyon.com/blog/introducing-spin-v1](https://www.fermyon.com/blog/introducing-spin-v1)
- [WebAssembly (Wasm): Past, Present, Future | Eröffnungs-Keynote BASTA! Spring 2023 in Frankfurt](https://yewtu.be/watch?v=0Bh_YcUWsiM)
- [Writing Server Side WebAssembly with Python | Complete Guide to Spin](https://yewtu.be/watch?v=neAnYfIcNLE)

## Wasm

---

- Resource utilization, With same compute power, more applications could be executed
- Speed, Wasm modules are boostrapped in no-time and fast at runtime
- Security, Wasm modules are isolated (sandbox) and have dedicated permissions
- Size, Wasm is tiny compared to containers or VMs

---

- WASI, WebAssembly System Interface, Spec only
- Provides system calls to Wasm modules
- Platform-agnostic, Wasm application could run om any WASI-compliant platform
- Designed to provide only essential system calls

---

- Wasi runtime, Delegtes system calls to system, Thin layer

---

- Serverless, No infrastructure management
- Wasm speed allows scale-down to 0
- Low impact on request performance

---

- Spin: Runtime, SDK, Developer Tooling
- `spin.toml`, Spin app Manifest

---

## Download and Install Spin

- [Download](https://github.com/fermyon/spin/releases/download/v1.3.0/spin-v1.3.0-windows-amd64.zip)
- [Install](https://developer.fermyon.com/spin/quickstart#install-spin)

## Spin Commands

```shell
spin template list
```

## Install Python Template

```shell
spin templates install --git https://github.com/fermyon/spin-python-sdk --update
```

## Install Tools

```shell
spin plugins update
```

Install the Python plugin to convert Python applications to Spin compatible modules.

```shell
spin plugin install py2wasm --yes
spin plugin install cloud --yes
```

## Create an Application

```shell
spin new
tree
```

## Build Application

```shell
cd wasm-py-demo
spin build
```

## Run Application

```shell
spin up
```

## Login to Fermyon

```shell
spin login
```

## Deploy Application on Fermyon Cloud

```shell
spin deploy
```

## Load tester

Downlod [here](https://hey-release.s3.us-east-2.amazonaws.com/hey_windows_amd64), rename to `.exe` and use.

```shell
 hey -n 20 -n 1000 https://stock-app-nydv3p97.fermyon.app
```
