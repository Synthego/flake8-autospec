# flake8-autospec #

flake8 plugin to check that `autospec=True` is used for mocks.

## Usage ##

.pre-commit-config.yaml

```yaml
  - repo: https://github.com/pycqa/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
        additional_dependencies: ['git+https://github.com/Synthego/flake8-autospec.git']
```

## Plugins ##

- _mock_autospec_
  - The following patching usages are covered:
    - `mock.patch`, `mock.patch.object`, and `mock.patch.multiple`
    - usage as class/method decorator, or as a context manager
  - __M100__: autospec keyword arg missing
  - __M101__: autospec keyword should be True

## Development ##

Running tests:

    tox

As an alternative to using `tox`, you may run `pytest` from within your own virtual environment:

    pip install -e .[test]
    pytest
