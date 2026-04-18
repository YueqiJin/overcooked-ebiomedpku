# Example workflow

This example follows the upstream DEBKS example pipeline.

## Prepare references

1. Index genome FASTA.

```bash
samtools faidx hg19.fa
```

2. Prepare sorted and tabix-indexed GTF.

```bash
grep -v '#' gencode.v19.annotation.gtf | sort -k 1,1 -k 4,4n | bgzip > gencode.v19.annotation.sort.gtf.gz
tabix gencode.v19.annotation.sort.gtf.gz
```

## Simulate data (optional)

```bash
mkdir dataset1
python sim_circ.py 0.01 dataset1 gencode.v19.annotation.sort.gtf.gz outJunction_mouse.txt

mkdir dataset2
python sim_circ2.py 0.01 dataset2 gencode.v19.annotation.sort.gtf.gz outJunction_mouse.txt
```

## Detect circRNA (example using CIRI2)

```bash
ls CIRI/*.ciri > samplelist.txt
DEBKS merge -s ciri2 -f samplelist.txt
```

## Count linear junctions (optional if already available)

```bash
ls bam/*/Aligned.sortedByCoord.out.bam > bamlist.txt
DEBKS count -c merge_pos.txt -f bamlist.txt -t 6
```

## Annotate circRNA lengths (optional)

```bash
DEBKS anno -c merge_pos.txt -m hg19.fa -g gencode.v19.annotation.sort.gtf.gz
```

## Detect DE circRNAs

```bash
DEBKS dec -c merge_circ.txt -l merge_linear.txt -t 20 -e anno_len.txt
```

Optional alternate linear-junction input:

```bash
DEBKS dec -c merge_circ.txt -l linear_jun.txt -t 20 -e anno_len.txt -o dec_star.txt
```
