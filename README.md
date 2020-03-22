#### Description

Generate Exploit Template

I've written this template generator to write my exploits.

#### Installation

##### Install from `pip`:
```bash
pip install expl
```

##### Install from source
1. clone it from repo:
```bash
git clone https://github.com/AlirezaKm/expl
```

2. Install from source:
```bash
cd expl
pip install -e .
```

#### Usage

```bash
$ expl
```
```text
Usage: expl [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  both    Generate a Template for Local and Remote
  local   Generate Local Template
  remote  Generate Remote Template

```
##### More Info about commands
```bash
$ expl local --help
```
```text
Usage: expl local [OPTIONS] FILE

  Generate Local Template

Options:
  -a, --arch TEXT      Architecture of Executable File  [default: x86_64]
  --os TEXT            OS of Executable File  [default: linux]
  -e, --endian TEXT    OS of Executable File  [default: little]
  -l, --loglevel TEXT  Log Level of pwntools  [default: info]
  -r, --realpath TEXT  using realpath for Executable File  [default: False]
  --libc TEXT          Address of LIBC
  -o, --output TEXT    write to output
  --help               Show this message and exit.
```


##### Generate a template for a Local Executable File
```bash
$ expl local vuln
```
```python
#!/usr/bin/python2

from pwn import *



context(arch='x86_64', os='linux', endian='little', log_level='info')


def info(s):
    log.info(s)


def exploit_(r):
    r.interactive()


if __name__ == '__main__':
 
    r = process(['vuln'])
    print(util.proc.pidof(r))
    pause()
    exploit(r)
```