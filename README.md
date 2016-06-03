Samitizer
==========

Python library for parsing SAMI file. Forked from [pysami][1] (thus license is preserved).


Installation
-----

```sh
# to use auto charset detection, you should install uchardet
sudo apt-get install uchardet

# virtual environment like `virtualenv` is recommended
virtualenv venv
source venv/bin/activate

# install
pip install samitizer
```

Usage
-----

```python
from __future__ import print_function
from samitizer import Smi

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

[1]: https://github.com/g6123/pysami "pysami"
