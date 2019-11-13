# KONSOL

### Build your own console

## Installation
```bash
pip install https://github.com/arissupriy/konsol/archive/master.zip
```

## Test

create name file ```test.py``` and copy script below :

```python
from konsol import Command, Konsol

def hello():
    print("hello")

command = Command()
command.add("hello", hello)

console = Konsol(
    command=command,
    command_name='your_console_name'
)

console.start()

```

and then run :

```bash
python test.py
```

result 
```bash
(your_console_name) ~ 
(your_console_name) ~ hello
.
.
.
create your best command line
```