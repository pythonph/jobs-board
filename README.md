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

### Styleguides

- [Design](https://github.com/pythonph/styleguide)
- [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python
- [Standard](http://standardjs.com/) for JavaScript

## License

[MIT](./LICENSE)
