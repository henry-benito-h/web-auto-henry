## Web-Auto-Henry — Pytest + Playwright

This repository contains a set of test examples and utilities for web automation. The project was originally built with Selenium examples, and it also includes support for Playwright-based tests via pytest-playwright.

This README provides quick setup and run instructions specifically for running tests with pytest and Playwright on Windows (PowerShell).

## Prerequisites

- Python 3.8+ (use your preferred virtual environment)
- Node is NOT required for the Python Playwright package; however, Playwright browsers must be installed using the Playwright CLI provided by the Python package.

## Install dependencies

From the repository root:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Install Playwright browsers

After installing the `playwright` package, install the browser binaries:

```powershell
python -m playwright install
# or install only specific browsers:
python -m playwright install chromium firefox webkit
```

Note: On CI you may prefer `python -m playwright install --with-deps` depending on the image.

## Running tests with pytest + Playwright

- Run all tests (this will run both pytest-playwright and other pytest tests):

```powershell
pytest -q
```

- Run only Playwright tests (if you place them under a folder or use -k to filter):

```powershell
pytest -q -k playwright
```

- Run with different browsers:

```powershell
python -m pytest tests/prestashop/play/test_navigation_play.py -vs --headed --browser chromium --browser-channel msedge
```

Playwright provides the `page`, `browser` and `browser_context` fixtures out of the box when `pytest-playwright` is installed.

Example minimal Playwright test (see `tests/test_playwright_example.py`):

```python
def test_example_page_title(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()
```

## Allure reporting (optional)

If you want to generate Allure reports, run pytest with the `--alluredir` option and then serve the results.

```powershell
pytest --alluredir=allure-results
# Then (requires Allure CLI installed):
allure serve allure-results
```

## Notes about this repository

- There are existing Selenium-based examples under `src/pages/selenium` and `tests/test_example_selenium.py`.
- Playwright-based tests can coexist with Selenium tests. Keep Playwright tests simple and use the `page` fixture for browser automation.
- Use `pytest.ini` and `tests/conftest.py` to add project-specific fixtures and command-line options.

## Troubleshooting

- If tests that use Playwright fail to start, ensure you ran `python -m playwright install` and that the virtual environment where `playwright` is installed is active.
- For CI, make sure the runner image has required libraries (libnss, libatk-1.0, etc.) or use Playwright's `--with-deps` option.

## Example commands summary (PowerShell)

```powershell
# Create & activate venv
python -m venv .venv; .\.venv\Scripts\Activate.ps1
# Install dependencies
pip install -r requirements.txt
# Install Playwright browsers
python -m playwright install
# Run tests
pytest -q
# Run and collect Allure results
pytest --alluredir=allure-results
```

If you'd like, I can also add a Playwright test folder structure or convert one Selenium test to Playwright as a follow-up.

---
Updated: README with pytest+Playwright setup and run instructions.
