# tap-msaccess

`tap-msaccess` is a Singer tap for Microsoft Access.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
# pip
pip install git+https://github.com/Matatika/tap-msaccess

pip install git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with fsspec http(s) support
pip install git+https://github.com/Matatika/tap-msaccess s3fs  # with fsspec s3 support
pip install git+https://github.com/Matatika/tap-msaccess adlfs  # with fsspec azure support

# pipx
pipx install git+https://github.com/Matatika/tap-msaccess

pipx install git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with fsspec http(s) support
pipx install git+https://github.com/Matatika/tap-msaccess s3fs  # with fsspec s3 support
pipx install git+https://github.com/Matatika/tap-msaccess adlfs  # with fsspec azure support

# poetry
poetry add git+https://github.com/Matatika/tap-msaccess

poetry add git+https://github.com/Matatika/tap-msaccess fsspec[http]  # with fsspec http(s) support
poetry add git+https://github.com/Matatika/tap-msaccess s3fs  # with fsspec s3 support
poetry add git+https://github.com/Matatika/tap-msaccess adlfs  # with fsspec azure support
```

## Configuration

### Accepted Config Options

Name | Required | Default | Description
--- | --- | --- | ---
`database_file` | Yes |  | Local or URL path to a Microsoft Access database `.mdb` or `.accdb` file
\* | | | Options for the [`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/) storage backend implementation dictated by the `database_file` URL protocol, such as [HTTP(S)](https://filesystem-spec.readthedocs.io/en/latest/api.html?highlight=http#fsspec.implementations.http.HTTPFileSystem), [S3](https://s3fs.readthedocs.io/en/latest/) or [Azure](https://github.com/fsspec/adlfs?tab=readme-ov-file#readme) (see [built-in implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html?highlight=http#built-in-implementations) and [other known implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html?highlight=http#other-known-implementations) for more information)

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
`database_file` | `http://github.com/Matatika/tap-msaccess/raw/main/sample_db/Books.accdb`<br>`https://github.com/Matatika/tap-msaccess/raw/main/sample_db/Books.accdb`

#### S3

Public read-only bucket

Key | Value
--- | ---
`database_file` | `s3://<bucket name>/<file path>`

#### Azure

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
