# Usage

## Command overview

```bash
DEBKS (merge | count | anno | dec) [options]
```

Commands:

- `merge`: merge circRNA junction information from other software outputs
- `count`: count linear junctions from BAM files
- `anno`: annotate circRNA positions and infer lengths
- `dec`: detect differentially expressed circRNAs

## merge

```text
DEBKS merge (-s software | -d designate) (-n name | -f file) [-b pos_based] [-o output]
```

Example:

```bash
DEBKS merge -s CIRI2 -n s1.ciri,s2.ciri,s3.ciri
```

## count

```text
DEBKS count -c circ_pos (-n name | -f file) [-l library_type] [-t threads] [-a hangover_len] [-o output]
```

Example:

```bash
DEBKS count -c merge_pos.txt -n s1.sort.bam,s2.sort.bam,s3.sort.bam
```

## anno

```text
DEBKS anno -c circ_pos -g gene_anno -m genome [-o output]
```

Example:

```bash
DEBKS anno -c merge_pos.txt -m hg19.fa -g gencode.v19.annotation.sort.gtf.gz
```

## dec

```text
DEBKS dec -c circ (-l linear | --c2 circ2) [-p] [-n sample_num] [-f filter] [-t threads] [-d cutoff] [-r read_len] [-a hangover_len] [-e circ_len] [--e2 circ2_len] [-o output]
```

Example:

```bash
DEBKS dec -c merge_circ.txt -l merge_linear.txt -n 3,3 -f 12 -t 20 -e anno_len.txt
```

Notes:

- `--c2` and `-l` are mutually exclusive.
- `-e` and `--e2` provide circRNA lengths to adjust junction-ratio calculation.

## DEC output fields

| Field | Description |
|:---:|---|
| chr | chromosome of circRNA |
| start | coordinate of start back-spliced site |
| end | coordinate of end back-spliced site |
| cjc_1 | circular-junction counts in group 1 |
| cjc_2 | circular-junction counts in group 2 |
| ljc_1 or cjc2_1 | linear or circular2 junction counts in group 1 |
| ljc_2 or cjc2_2 | linear or circular2 junction counts in group 2 |
| adj_cjc_len | length-adjust term for cjc |
| adj_ljc_len | length-adjust term for ljc |
| pbsi1 | circular-junction ratio in group 1 |
| pbsi2 | circular-junction ratio in group 2 |
| delta_pbsi | average difference between pbsi1 and pbsi2 |
| P | significance of delta_pbsi |
| FDR | Benjamini-Hochberg corrected FDR |

For importing CIRIquant outputs into DEBKS, see [Import from CIRIquant](import-from-ciriquant.md).
