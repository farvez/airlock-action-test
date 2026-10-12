# Airlock Action test

A small example repository that runs its tests in an Airlock sandbox with
[Run in Airlock Sandbox](https://github.com/marketplace/actions/run-in-airlock-sandbox).

- `calc.py` and `test_calc.py`: an ordinary module and its tests.
- `test_sandbox.py`: tests that prove where they ran. They pass only inside an Airlock sandbox that can
  reach PyPI and nothing else.
- `.github/workflows/airlock.yml`: runs everything on each push, then saves the test report as an
  artifact.

To use it, add an Airlock API key as the repository secret `AIRLOCK_API_KEY`.
