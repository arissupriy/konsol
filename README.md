# KONSOL

### Build your own console

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