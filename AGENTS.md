# AGENTS.md

## Build/Test Commands
- `just test` - Run all tests with coverage
- `just test tests.test_bootstrap_form` - Run single test module
- `just test tests.test_bootstrap_form.BootstrapFormTestCase.test_exclude` - Run single test method
- `just format` - Format code (ruff format + ruff check --fix)
- `just lint` - Check linting without fixing
- `just tests` - Run tests across all Python/Django versions (tox)

## Code Style
- **Line length**: 120 characters (ruff)
- **Formatter**: ruff (rules: D, E, F, I, UP)
- **Imports**: stdlib → third-party (django) → first-party (django_bootstrap5, app)
- **Naming**: PascalCase for classes, snake_case for functions/variables, UPPER_SNAKE_CASE for constants
- **Types**: Minimal type annotations; used selectively in base classes (ClassVar, Literal, return types)
- **Docstrings**: Multi-line with summary first; RST-style for template tags; not required on all functions

## Testing Patterns
- Test classes inherit from `tests.base.BootstrapTestCase`
- Use `self.render(template_string, context)` to render templates
- Use `self.assertHTMLEqual()` and `self.assertInHTML()` for HTML comparison
- Test forms: define inline as `class MyTestForm(forms.Form)` in test files
