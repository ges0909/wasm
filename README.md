# Webassembly (Wasm)

## Links

- [https://www.fermyon.com/blog/introducing-spin-v1](https://www.fermyon.com/blog/introducing-spin-v1)
- [WebAssembly (Wasm): Past, Present, Future | Eröffnungs-Keynote BASTA! Spring 2023 in Frankfurt](https://yewtu.be/watch?v=0Bh_YcUWsiM)
- [Writing Server Side WebAssembly with Python | Complete Guide to Spin](https://yewtu.be/watch?v=neAnYfIcNLE)

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

## Run Apllication

```shell
spin up
```

## Deploy Application on Fermyon Cloud

```shell
spin deploy
```
