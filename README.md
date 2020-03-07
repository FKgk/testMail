# smail

## How to install
```
git clone https://github.com/FKgk/simple-send-mail.git
```
or
```
pip install smail
```

## Dependency
- this package don't need any reqiurements
- need built-in module (email, smtplib, re)

## Example
```
from smail import Mail

mail = Mail("sender email", "app password")

mail.send("receiver(s) email", "title", "content")

mail.close()
```

### If you want to check validation
```
mail.valid("email")
```
- return true or flase

## Reference
- https://docs.python.org/3/library/smtplib.html
