Resamplr: Resample FLACs Intelligently
---

Resamplr is designed to quickly and intelligently resample FLACs based on the samplerate of source files.


###Installation

Depends on `sox`, `pysox`, and `flac`.

On Debian: `sudo apt-get install sox flac libsox-fmt-all && pip install sox`

Once they are installed, simply run `make install` from this project's directory.

###Usage

```
usage: resamplr [-h] [-v] [--bitdepth BITDEPTH] [--samplerate SAMPLERATE] source dest

Resample FLACs intelligently.

positional arguments:
  source                Directory of FLACs to resample.
  dest                  Destination directory for resampled FLACs.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --bitdepth BITDEPTH, -b BITDEPTH
                        Desired bit depth for resampled FLACs. Default: 16
  --samplerate SAMPLERATE, -s SAMPLERATE
                        Desired samplerate for resampled FLACs. Default:
                        Automatically choose 44100 or 48000
```