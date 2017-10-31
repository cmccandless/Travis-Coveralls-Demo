# Travis-Coveralls-Demo

[![Build Status](https://travis-ci.org/cmccandless/Travis-Coveralls-Demo.svg?branch=master)](https://travis-ci.org/cmccandless/Travis-Coveralls-Demo) [![Coverage Status](https://coveralls.io/repos/github/cmccandless/Travis-Coveralls-Demo/badge.svg?branch=master)](https://coveralls.io/github/cmccandless/Travis-Coveralls-Demo?branch=master)

Tutorial for setting up a new Github Repository with [Travis-CI](https://travis-ci.org/) and [Coveralls](https://coveralls.io/) support.

Travis-CI and Coveralls are not limited to [Python](https://www.python.org/) repositories, but we will use Python in this tutorial.

## Steps

### 1) Add [source code](https://github.com/cmccandless/Travis-Coveralls-Demo/blob/9751a043c14376c40e60ed2c3ef4945cb56ca8e5/convert.py)

### 2) Add [unit tests](https://github.com/cmccandless/Travis-Coveralls-Demo/blob/9751a043c14376c40e60ed2c3ef4945cb56ca8e5/convert_test.py)

### 3) Travis-CI

#### 3.1) Configure

##### 3.1.1) Create .travis.yml

```YML
# Most Travis scripts will probably not need sudo enabled
sudo: false

# Language of your repository
language: python

# Language versions for Travis to test
python:
  - 2.7
  - 3.3
  - 3.4
  - 3.5
  - 3.6
  - nightly

# Test matrix settings
matrix:
  # Ignore failures for unstable versions
  allow_failures:
    - python: nightly

# Install dependencies here (apt-get, pip, etc.)
install:
  - pip install -r requirements-travis.txt

# Code style checks are often run here
# See http://flake8.pycqa.org/en/latest/ for more info on flake8
before_script:
  - flake8

# Call your CI script here
script:
  - pytest -v
```

##### 3.1.2) (Optional) Create requirements-travis.txt

*Filename is not important, and contents could just as easily be inserted into `.travis.yml`*

#### 3.2) Go to [Travis-CI.org](https://travis-ci.org/)

##### 3.2.1) Click `Sign in with GitHub`

##### 3.2.2) Go to [profile](https://travis-ci.org/profile/) and follow instructions

#### 3.3) Trigger a new build manually or by pushing new commits

#### 3.4) (Optional) Add badge to repository README

Click on the badge
[![Build Status](https://travis-ci.org/cmccandless/Travis-Coveralls-Demo.svg?branch=master)](https://travis-ci.org/cmccandless/Travis-Coveralls-Demo)
on your build results page.

### 4) Coveralls

#### 4.1) Enable

Follow steps at `https://coveralls.io/github/USERNAME/REPOSITORY`

#### 4.2) Configure coverage

.coveragerc

```ini
[report]
omit =
    */python?.?/*
    *__init__*
    *_test.py
```

#### 4.3) Run coverage and coveralls in Travis-CI build

``` YML
# Call your CI script here
script:
  - python -m pytest -v
  - coverage run -m pytest -v

after_success: coveralls
```

#### 4.4) Trigger another new Travis-CI build

#### 4.5) (Optional) Add badge to repository README

Click on "EMBED" next to
[![Coverage Status](https://coveralls.io/repos/github/cmccandless/Travis-Coveralls-Demo/badge.svg?branch=master)](https://coveralls.io/github/cmccandless/Travis-Coveralls-Demo?branch=master)
inside the "BADGE YOUR REPO: \<repository\>" banner at the bottom of your Coveralls build results page.