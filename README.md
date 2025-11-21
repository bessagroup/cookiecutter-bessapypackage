<p align="center">
  <a href=""><img alt="logo" src="https://user-images.githubusercontent.com/25851824/200928507-a65327f9-bc70-4c12-beaa-bc6ba74d968e.svg" width="60%"></a>
</p>

# Bessa Group Cookiecutter Python repository template


| [**GitHub**](https://github.com/bessagroup/cookiecutter-bessapypackage) |

**First publication:** July 31, 2025

***

## Summary

This repository serves as a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) template for Python code.
Cookiecutter is a command-line utility that creates projects from project templates, e.g., Python packages. It is a great way to quickly set up a new Python package with a standard structure and best practices, and it replaces the need to manually create the boilerplate code for a new Python package.

Upon running the template, it will prompt you for some information about your new package, such as the package name, author name, and email address. After you provide this information, Cookiecutter will generate a new directory with the structure of a Python package.

The template is compliant to the [Bessa Research Group Python Development Code of Conduct](https://github.com/bessagroup/python_code_of_conduct). This template is adopted from the [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) template by Audrey M. Roy Greenfeld.
## Statement of need

Members of the Bessa Research Group can use this cookiecutter template to create new Python repositories. The template is compliant to the [Bessa Research Group Python Development Code of Conduct](https://github.com/bessagroup/python_code_of_conduct).

## Authorship

**Authors**:
- Martin van der Schelling ([M.P.vanderSchelling@tudelft.nl](mailto:M.P.vanderSchelling@tudelft.nl))

**Authors afilliation:**
- Bessa Research Group @ Delft University of Technology

**Maintainer:**
- Martin van der Schelling ([M.P.vanderSchelling@tudelft.nl](mailto:M.P.vanderSchelling@tudelft.nl))

**Maintainer afilliation:**
- Bessa Research Group @ Delft University of Technology


## Getting started

Install Cookiecutter in your Python environment:

```bash
pip install cookiecutter
```

Navigate to the directory where you want to create your new Python package project, and run the following command:

```bash
cookiecutter https://github.com/bessagroup/cookiecutter-bessapypackage.git
```

You will be prompted to enter some information about your new package, such as the package name, author name, and email address. After you provide this information, Cookiecutter will generate a new directory with the structure of a Python package.

**IMPORTANT: You do not clone this respository and work from it directly. The files contain template variables that need to be filled in when creating a new project. Instead, you use Cookiecutter to generate a new project based on this template.**

### Filling in your project details

When generating a new project using Cookiecutter, you are prompted to provide several fields that are then automatically substituted into project files such as `pyproject.toml`, `README.md`, package directory names, CI configuration, and licensing metadata. Below is an explanation of each field in this configuration template.
| Keyword                      | Description                                                    | Used In                                                                                               | Example                          |
|------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------|
| `full_name`                  | Your full personal name                                        | Copyright headers, `LICENSE.md`, project metadata (author in `pyproject.toml`)                        | `Martin van der Schelling`       |
| `email`                      | Primary contact email for the maintainer                      | `pyproject.toml` (`author_email`), support/contact in docs                                            | `name@example.com`               |
| `affiliation`                | Institutional or company affiliation                           | `README.md` author section, documentation metadata                                                    | `TU Delft`                       |
| `github_username`            | GitHub username or organization name                           | Repository URL config, GitHub links (issues), `README.md` badges/contributing                         | `mpvanderschelling`              |
| `pypi_package_name`          | Name of the package on PyPI                                    | `pyproject.toml` metadata, PyPI uploads, `README.md` title                                             | `my-python-package`              |
| `project_name`               | Human-readable project name                                    | `README.md` title, documentation title pages, user-facing display names                               | `Python Boilerplate`             |
| `project_slug`               | Machine-safe project name (import path)                        | Package folder name, internal references                                                              | `my_python_package`              |
| `project_short_description`  | One-sentence summary of the project                            | `README.md` introduction, PyPI summary, docs headers                                                  | `A starter template for Python.` |
| `project_keywords`           | Comma-separated descriptive keywords                           | PyPI search indexing, metadata in `pyproject.toml`                                                    | `template, boilerplate, python`  |
| `pypi_username`              | Username for the PyPI account (often GitHub username)          | Publishing scripts, CI deployment configuration                                                       | `mpvanderschelling`              |
| `first_version`              | Initial version number                                          | `pyproject.toml` version field                                                                        | `0.1.0`                          |
| `minimal_python_version`     | Lowest supported Python version                                | `pyproject.toml` dependencies, CI matrix, installation requirements                                   | `3.11`                           |


### Enabling certain behaviour

After filling in the fields above, a new project directory is created. Some features of the template are disabled by default in order to automatically run unwanted services, such as publishing to PyPI of automatically linting the code. 

To enable these features, you need to uncomment the content of the following files:

| File / Workflow                          | Purpose                                                                                     | Action Required                                           |
|------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `.pre_commit_config.yaml`                | Configure pre-commit hooks for automatic code linting and formatting                        | Uncomment the hooks you want to enable                    |
| `.github/workflows/build_docs.yml`       | Generate and upload documentation artifacts automatically                                   | Uncomment to enable documentation build workflow          |
| `.github/workflows/pull_request.yml`     | Automatically run tests on pull requests                                                    | Uncomment steps to enable PR testing                      |
| `.github/workflows/release.yml`          | Publish package to PyPI when pushing to `main`                                              | Uncomment steps to enable automatic PyPI releases         |


## Community Support

If you find any **issues, bugs or problems** with this template, please use the [GitHub issue tracker](https://github.com/bessagroup/cookiecutter-bessapypackage/issues) to report them.


## License

Copyright 2025, Martin van der Schelling

All rights reserved.

This project is licensed under the BSD 3-Clause License. See [LICENSE](https://github.com/bessagroup/cookiecutter-bessapypackage/blob/main/LICENSE) for the full license text.

