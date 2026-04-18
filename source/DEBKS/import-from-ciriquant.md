# Import from CIRIquant

DEBKS can import circular junction count (CJC) and linear junction count (LJC)
matrices from CIRIquant results with the optional `prep_DEBKS` utilities provided
in the DEBKS repository.

## Required scripts

The repository includes:

- `script/prep_DEBKS`
- `script/prep_DEBKS.py`

These utilities are adapted for CIRIquant result preparation.

## Placement

Place the helper files into the CIRIquant installation paths:

- `prep_DEBKS.py` into the CIRIquant library directory
- `prep_DEBKS` into the CIRIquant executable/bin directory

## Usage

### Prepare CIRIquant output files list
```
CONTROL1 ./c1/c1.gtf C 1
CONTROL2 ./c2/c2.gtf C 2
CONTROL3 ./c3/c3.gtf C 3
CASE1 ./t1/t1.gtf T 1
CASE2 ./t2/t2.gtf T 2
CASE3 ./t3/t3.gtf T 3
```

The first three columns is required by default. For paired sample, the fourth column is required to specify the pairing information. For unpaired sample, the fourth column can be omitted.

### Run `prep_DEBKS`

```bash
prep_DEBKS -i FILE --lib FILE --circ FILE --bsj FILE --fsj FILE --ratio FILE
```

Options:

- `-i FILE`: input sample list 
- `--lib FILE`: output library information file
- `--circ FILE`: output circRNA annotation file, typically `merge_pos.txt`
- `--bsj FILE`: output circRNA back-splice junction counts, typically `merge_circ.txt`
- `--fsj FILE`: output forward-splice/linear junction counts, typically `merge_linear.txt`
- `--ratio FILE`: output circRNA junction-ratio matrix

## Outputs for downstream DEBKS analysis

Typical generated files are:

- `merge_pos.txt`
- `merge_circ.txt`
- `merge_linear.txt`

These outputs can be used as follows:

- Use `merge_pos.txt` with `DEBKS anno` to annotate circRNAs and infer lengths.
- Use `merge_circ.txt` and `merge_linear.txt` with `DEBKS dec` to detect DE circRNAs.