# django-bootstrap5 (Fork)

This is a fork of [zostera/django-bootstrap5](https://github.com/zostera/django-bootstrap5) that extends the `bootstrap_field` template tag with additional functionality inspired by [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks).

## Fork Enhancements

The `bootstrap_field` tag now accepts arbitrary HTML attributes that are passed directly to the input widget. This eliminates the need for django-widget-tweaks when using django-bootstrap5.

### Features

- **Arbitrary HTML attributes**: Pass any attribute directly to the widget (e.g., `data-*`, `aria-*`, `autocomplete`)
- **Hyphenated attribute names**: Use hyphens directly in attribute names (e.g., `data-foo="bar"`)
- **Boolean attributes**: Support for valueless attributes (e.g., `disabled`, `readonly`)
- **Framework support**: Works with htmx, Alpine.js, Vue.js, and other JavaScript frameworks
- **Backward compatible**: Underscore-to-hyphen conversion still works (e.g., `data_foo` becomes `data-foo`)

### Usage Examples

```jinja2
{% load django_bootstrap5 %}

{# Basic HTML attributes #}
{% bootstrap_field form.email autocomplete="off" %}
{% bootstrap_field form.search placeholder="Search..." aria-label="Search" %}

{# Data attributes #}
{% bootstrap_field form.name data-validate="true" data-max-length="100" %}

{# Boolean attributes #}
{% bootstrap_field form.readonly_field readonly %}
{% bootstrap_field form.disabled_field disabled %}

{# htmx attributes #}
{% bootstrap_field form.search hx-get="/search" hx-trigger="keyup changed delay:500ms" hx-target="#results" %}

{# Alpine.js attributes #}
{% bootstrap_field form.toggle x-data="{ open: false }" x-on:click="open = !open" %}
{% bootstrap_field form.input x-bind:class="{ 'is-valid': valid }" %}

{# Vue.js attributes #}
{% bootstrap_field form.input v-model="message" @input="handleInput" %}
{% bootstrap_field form.input v-bind:class="{ active: isActive }" %}
```

---

## Original README

[![Tests](https://github.com/zostera/django-bootstrap5/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/zostera/django-bootstrap5/actions?workflow=test)
[![Coverage Status](https://coveralls.io/repos/github/zostera/django-bootstrap5/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-bootstrap5?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-bootstrap5.svg)](https://pypi.python.org/pypi/django-bootstrap5)

Bootstrap 5 for Django.

## Goal

The goal of this project is to seamlessly blend Django and Bootstrap 5.

## Status

Ready for production. Issues and pull requests welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Requirements

This package requires a combination of Python and Django that is currently supported.

See "Supported Versions" on https://www.djangoproject.com/download/.

This package uses [uv](https://github.com/astral-sh/uv) and [just](https://github.com/casey/just) for local development.

## Documentation

The full documentation is at https://django-bootstrap5.readthedocs.io/

## Installation

1. Install using pip:

    ```console
    pip install django-bootstrap5
    ```

2. Add to `INSTALLED_APPS` in your `settings.py`:

   ```python
   INSTALLED_APPS = (
       # ...
       "django_bootstrap5",
       # ...
   )
   ```

3. In your templates, load the `django_bootstrap5` library and use the `bootstrap_*` tags. See example below.

## Example template

```jinja2
{% load django_bootstrap5 %}

<form action="/url/to/submit/" method="post" class="form">
    {% csrf_token %}

    {% bootstrap_form form %}

    {% bootstrap_button button_type="submit" content="OK" %}
    {% bootstrap_button button_type="reset" content="Cancel" %}
</form>
```

## Example app

An example app is provided in the folder `example`. You can run the example app with this command:

```console
just example
```

## Bugs and suggestions

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/zostera/django-bootstrap5/issues

## License

You can use this under BSD-3-Clause. See [LICENSE](LICENSE) file for details.

## Author

Developed and maintained by [Zostera](https://zostera.nl).

Original author: [Dylan Verheul](https://github.com/dyve).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.

Please see [AUTHORS](AUTHORS) for a list of contributors.
