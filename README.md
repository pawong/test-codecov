# Testing with Codecov.io

![Tests](https://github.com/pawong/test-codecov/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/pawong/test-codecov/branch/master/graph/badge.svg)](https://codecov.io/gh/pawong/test-codecov)

### Build

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Test

```bash
$ pytest
======================= test session starts ========================
platform darwin -- Python 3.10.9, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/pwong/Code/test-codecov
plugins: cov-4.1.0
collected 5 items

tests/test_fibonacci.py ..                                   [ 40%]
tests/test_strings_for_digits.py ...                         [100%]

======================== 5 passed in 0.03s =========================
```
