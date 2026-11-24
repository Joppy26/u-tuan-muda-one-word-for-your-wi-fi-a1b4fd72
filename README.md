# One Word for Your Wi-Fi

[![Competition](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Joppy26/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Joppy26/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the [One Word for Your Wi-Fi bounty on make.fun](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) ($2 winner-takes-all).

## The word

> leftonread

Full bars, nothing loads, messages stuck on sending at 1am. The router
sees you, it just never replies. That is the whole relationship.

**Character count: 10** (limit 20). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed word to `entry.txt` inside the output
directory, `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/wifi-out python3 main.py
cat /tmp/wifi-out/entry.txt
```
