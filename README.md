# tap-msaccess

`tap-msaccess` is a Singer tap for Microsoft Access.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMatatika%2Ftap-msaccess%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies.python&label=python)](https://docs.python.org/3/)
[![Singer SDK version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMatatika%2Ftap-msaccess%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies%5B%22singer-sdk%22%5D&label=singer-sdk)](https://sdk.meltano.com/en/latest/)
[![License](https://img.shields.io/github/license/Matatika/tap-msaccess)](https://github.com/Matatika/tap-msaccess/blob/main/LICENSE)
[![Code style](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fruff%2Fmain%2Fassets%2Fbadge%2Fformat.json)](https://docs.astral.sh/ruff/)
[![Test tap-msaccess](https://github.com/Matatika/tap-msaccess/actions/workflows/test.yml/badge.svg)](https://github.com/Matatika/tap-msaccess/actions/workflows/test.yml)

## Installation

```bash
# pip
pip install git+https://github.com/Matatika/tap-msaccess

pip install git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with http(s) support
pip install git+https://github.com/Matatika/tap-msaccess fsspec[s3]  # with s3 support
pip install git+https://github.com/Matatika/tap-msaccess fsspec[abfs]  # with azure support

# pipx
pipx install git+https://github.com/Matatika/tap-msaccess

pipx install git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with http(s) support
pipx install git+https://github.com/Matatika/tap-msaccess fsspec[s3]  # with s3 support
pipx install git+https://github.com/Matatika/tap-msaccess fsspec[abfs]  # with azure support

# poetry
poetry add git+https://github.com/Matatika/tap-msaccess

poetry add git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with http(s) support
poetry add git+https://github.com/Matatika/tap-msaccess fsspec[s3]  # with s3 support
poetry add git+https://github.com/Matatika/tap-msaccess fsspec[abfs]  # with azure support
```

## Configuration

### Accepted Config Options

Name | Required | Default | Description
--- | --- | --- | ---
`database_file` | Yes |  | Local or URL path to a Microsoft Access database `.mdb` or `.accdb` file
\*<br>`connection_params` | | | Any parameters for the [`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/) storage backend implementation dictated by the `database_file` URL protocol, such as [HTTP(S)](https://filesystem-spec.readthedocs.io/en/latest/api.html#fsspec.implementations.http.HTTPFileSystem), [S3](https://s3fs.readthedocs.io/en/latest/) or [Azure](https://github.com/fsspec/adlfs?tab=readme-ov-file#readme) (see [built-in implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations) and [other known implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations) for more information)<br><br>These can be passed directly as top-level config (i.e. same as `database_file`) or via the `connection_params` setting as a JSON-object value - if both are provided, the configurations are merged, with values from `connection_params` taking precedence

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-msaccess --about
```

### Examples

#### Local

Key | Value
--- | ---
`database_file` | `sample_db/Books.accdb`<br>`<absolute path to repo>/sample_db/Books.accdb`<br>`local://sample_db/Books.accdb`<br>`local://<absolute path to repo>/sample_db/Books.accdb`<br>`file://sample_db/Books.accdb`<br>`file://<absolute path to repo>/sample_db/Books.accdb`

#### HTTP(S)

Key | Value
--- | ---
`database_file` | `http://github.com/Matatika/tap-msaccess/raw/main/sample_db/Books.accdb`<br>`https://github.com/Matatika/tap-msaccess/raw/main/sample_db/Books.accdb`<br>`https://matatikaartifacts.blob.core.windows.net/tap-msaccess/Books.accdb`

#### S3

Public read-only bucket

Key | Value
--- | ---
`database_file` | `s3://tap-msaccess/Books.accdb`
`anon` | `true`

Private bucket

Key | Value
--- | ---
`database_file` | `s3://<bucket name>/<file path>`
`key` | `<access key id>`
`secret` | `<secret access key>`

#### Azure

Public read-only storage blob

Key | Value
--- | ---
`database_file` | `az://tap-msaccess/Books.accdb`
`account_name` | `matatikaartifacts`

Private storage blob

Key | Value
--- | ---
`database_file` | `az://<container name>/<file path>`
`account_name` | `<account name>`
`account_key` | `<account key>`

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

## Usage

You can easily run `tap-msaccess` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-msaccess --version
tap-msaccess --help
tap-msaccess --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-msaccess` CLI interface directly using `poetry run`:

```bash
poetry run tap-msaccess --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-msaccess
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-msaccess --version
# OR run a test `elt` pipeline:
meltano elt tap-msaccess target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
