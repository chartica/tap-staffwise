# tap-staffwise

`tap-staffwise` is a Singer tap for Staffwise.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-staffwise
```

Install from GitHub:

```bash
pipx install git+git@github.com:chartica/tap-staffwise.git
```

-->

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-staffwise --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-staffwise --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-staffwise` by itself or in a pipeline using [Meltano](https://meltano.com/).

## Installing the Tap from a project file
Here is a step-by-step guide to using the Tap in your Meltano project folder:
1. Move to the directory which you want your Meltano project to be stored in, and have the tap folder cloned here from GitHub.
2. Run ```cd my_project``` to move into your project folder.
3. Run ```meltano init``` in your terminal and set the project name.
4. Run ```meltano add --custom extractor tap-staffwise``` in your terminal.
5. Use the default directory value.
6. Set pip_url to the path of the Tap folder. For the purpose of this guide, use ```-e ../tap-staffwise``` as the Tap will be installed in your local directory.
7. Use the default executable name.
8. Insert the following line into the settings field to setup the configuration menu: ```api_key:password, subdomain:string, reporting_id:string, start_date:string, stop_date:string```
9. Now that the Tap is installed, run ```meltano add loader target-jsonl``` and ```meltano add loader target-csv``` to install the loaders of the file types you want to extract the data to.
10. Set the values for api_key (required), subdomain (required), reporting_id (required), start_date (optional: default value is "2021-01-01") and stop_date (optional: default value is "2024-08-30") using ```meltano config tap-staffwise set --interactive``` 
11. Run the Tap using ```meltano run tap-staffwise target-jsonl``` to extract the data from the API. This will be stored in the output directory in your Meltano project.

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

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

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
