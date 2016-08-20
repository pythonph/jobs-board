# PythonPH Jobs Board

[![Build Status](https://semaphoreci.com/api/v1/pythonph/jobs-board/branches/master/badge.svg)](https://semaphoreci.com/pythonph/jobs-board)

## Development

### Requirements

- Python 3.5.x
- Node 4.x
- PostgreSQL 9.4+

### Setup

1. Install dependencies

  ```sh
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  npm install
  ```

2. Setup database

  ```
  createuser -P pythonph
  createdb -O pythonph jobsboard
  ```

3. Create configuration file

  ```sh
  cat .env
  DEBUG=True
  SECRET_KEY=secret
  DATABASE_URL=postgres://pythonph:password@localhost/jobsboard
  ```

4. Run migrations

  ```sh
  ./manage.py migrate
  ```

5. Create admin user

  ```sh
  ./manage.py createsuperuser
  ```

6. Run development server

  ```sh
  ./manage.py runserver
  ```

### Running the tests

  We use `py.test` as our test runner. It is currently configured to run
  the files inside directories named `tests` inside the sub-apps.

  Example: the tests for the `jobsboard.jobs` sub-app are inside
  `jobsboard/jobs/tests/`

  Basic usage:
  ```
  py.test
  ```

  py.test recreates the test DB every time. The time difference will
  become more noticeable once we have a lot of models in the app.

  To get around this, we can add `--reuse-db` to skip the db creation step.
  Take note that this doesn't reuse the existing DB for the current run, but
  for the next one.
  ```
  py.test --reuse-db
  ```

  If you introduced new fields or new models and use `--reuse-db` when running the
  test, you need to add `--create-db` so it will recreate the DB that includes
  you new fields or models.
  ```
  py.test --create-db
  ```

  You may also combine `--reuse-db` and `--create-db` so that it will create a new DB
  for this run, but reuse the test DB in the succeeding runs.
  ```
  py.test --create-db --reuse-db
  ```

### Styleguides

- [Design](https://github.com/pythonph/styleguide)
- [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python
- [Standard](http://standardjs.com/) for JavaScript

## License

[MIT](./LICENSE)
