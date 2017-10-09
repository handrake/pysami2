Pysami2
==========

Python library for parsing SAMI file. Forked from [samitizer][1] (thus license is preserved).


Installation
-----

```sh
# virtual environment like `virtualenv` is recommended
virtualenv venv
source venv/bin/activate

# install
pip install pysami2
```

Usage
-----

```python
from __future__ import print_function
from pysami2 import Smi

smi = Smi('sample.smi')
print(smi.subtitles[0].content['KRCC'])
vtt_text = smi.convert('vtt', lang='KRCC')
plain_text = smi.convert('plain', lang='KRCC')
```

Test
-----

```bash
python -m tests.test
```

[1]: https://github.com/theeluwin/samitizer "samitizer"
