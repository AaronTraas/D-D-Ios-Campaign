# Ruins puzzle

In the basement floor below the ruins near the crossroads on the road to Red Hawk, we encountered the following puzzle:

3 windows with 2 letters each, and a lever under each, and a central lever. Looks like:


| 1  | 2  | 3   |
|----|----|-----|
| AB | TI | US  |


Pulling a lever changes the letters. After 8 pulls, rotates back to the first. Looks like:


| 1  | 2  | 3   |
|----|----|-----|
| AB | TI | US  |
| FR | DR | TON |
| XI | A  | RY  |
| VI | CA | NLE |
| PO | I  | RLE |
| EK | RE | ZA  |
| QA | NE | PIN |
| RU | O  | ON  |

Found a coin with the letters “O K M” on it.

Lined up the boxes so it spelled

| 1  | 2  | 3   |
|----|----|-----|
| PO | TI | ON |


And pulled the central lever, and it triggered a draining spell on the party.

So I did the only rational thing, made a python script to generate all possible combinations, their reverses, and also interspersed the coin letters, and checked for dictionary words.

This python script requires the [PyEnchant package](https://pypi.org/project/pyenchant/)

You should be able run it with:

```bash
pip install pyenchant
python combo_puzzle_solution.py
```

Unfortunately, out of the 6144 combinations, the only dictionary word is "POTION"