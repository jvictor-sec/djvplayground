## Setup

Install all the required libraries using the command below

```bash
pip install -r requirements.txt 
```

Save '.env-example' file as '.env' and configure all environment variables

To setup SECRET_KEY variable, use the command below to get a secret key for yourself

```bash
# Windows
python manage.py getsecretkey
```

```bash
# Linux
python3 manage.py getsecretkey
```

Encrypt the secret key using the command below 

```bash
# Windows
python manage.py crypto 'your_key'
```

```bash
# Linux
python3 manage.py crypto 'your_key'
```

With the encrypted key, you can set the SECRET_KEY environment variable

This encryption process should be done with MYSQLPASSWORD variable aswell
