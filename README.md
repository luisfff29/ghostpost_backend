# Ghost Post API

The purpose of this project is to build a React front-end [https://github.com/luisfff29/ghostpost_frontend](https://github.com/luisfff29/ghostpost_frontend/) that interfaces with Django Rest Framework back-end [https://github.com/luisfff29/ghostpost_backend](https://github.com/luisfff29/ghostpost_backend/) runninng on the same machine.

The GhosPost Machine is a website where people can anonymously post Boasts or Roasts of whatever they want. Like Twitter, there is a character limit: 280 characters.

### Front-End:

- GET, and POST endpoints for boasts and roasts
- POST endpoints for voting on boasts and roasts

## Installation

Use the package manager [poetry](https://python-poetry.org/) to start a virtual environment:

```bash
poetry shell
```

Then, install all the dependencies required for this project:

```bash
poetry install
```

Don't forget to run the respective migrations:

```bash
    python manage.py migrate
```

Finally, you are ready to run the server with

```bash
python manage.py runserver
```

and check out the Ghost Post API built with Django in this [link](http://localhost:8000/api/posts/).
