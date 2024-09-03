# tap-staffwise

`tap-staffwise` is a Singer tap for Staffwise.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
pipx install git+git@github.com:chartica/tap-staffwise.git
```

## Configuration

### Accepted Config Options
In order to use this tap, you will need a Staffwise Endpoint URL (e.g. https://subdomain.staffed.it/reporting/api/get-data/{report-id}). Accepted config parameters are:

- API Key: API Key to authenticate requests and access the API
- Subdomain: Subdomain you would like to pull data from
- Reporting ID: Reporting ID of each report
- Start Date (optional): The start date for filtering results in the API call
- Stop Date (optional): The end date for filtering results in the API call

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-staffwise --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

## Usage

You can easily run `tap-staffwise` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-staffwise --version
tap-staffwise --help
tap-staffwise --config CONFIG --discover > ./catalog.json
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

You can also test the `tap-staffwise` CLI interface directly using `poetry run`:

```bash
poetry run tap-staffwise --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-staffwise
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-staffwise --version
# OR run a test `elt` pipeline:
meltano elt tap-staffwise target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
