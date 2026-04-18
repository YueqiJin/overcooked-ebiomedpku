# Usage

TERA is composed of TE identification (`TERA detect`), annotation (`TERA anno`), and quantification (`TERA quant`).

## Input files

```text
RNA sequencing files: paired end, in FASTQ format (fastq or fastq.gz)
TE reference: TE annotation in BED format (8 fields: chrom, chromStart, chromEnd, ID, name, strand, family, class) and GTF format (use script/TEbedtogtf.R).
Reference genome: reference genome sequence (FASTA) and annotation (GTF) are required. You can create genome index manually before running TERA.
```

## TERA

```text
usage: TERA [-h] {detect,anno,quant} ...

TERA: pipeline for Transposable Element-derived RNA Analysis

positional arguments:
  {detect,anno,quant}  sub-command help
    detect        detect help
    anno          anno help
    quant         quant help

optional arguments:
  -h, --help      show this help message and exit
```

## TERA detect

TERA detect is designed for teRNA detection.

```text
usage: tera.py detect [-h] -fq1 FASTQ1 -fq2 FASTQ2 --TE_bed TE_BED --TE_gtf
                      TE_GTF -r REF_GENOME -a ANNOTATION [-s {RF,FR}]
                      [-o OUTPUT_DIR] [-p PREFIX] [-m {1,2}] [-S STAR_INDEX]
                      [-G GMAP_INDEX] [-g GMAP_INDEX_NAME] [-t NTHREAD]
                      [--genomeSAindexNbases GENOMESAINDEXNBASES]
                      [--nthreadsort NTHREADSORT] [--nRAMsort NRAMSORT]
                      [--nRAMassem NRAMASSEM] [--max_intron MAX_INTRON]
                      [--min_identity MIN_IDENTITY]
                      [--min_coverage MIN_COVERAGE]
```

Main outputs:

1. `${prefix}.gtf` (TE transcripts)
2. `${prefix}_TE_exon.bed` (TE exons): 11 columns for chromosome, start, end, transcript_id, gene_id, strand, exon_type, TE_ID, TE_name, TE_family, TE_class

## TERA anno

TERA anno is designed for teRNA annotation.

```text
usage: tera.py anno [-h] [-i INPUT] [--TE_bed TE_BED] [-o OUTPUT_DIR]
                    [-p PREFIX] [-a ANNOTATION] [--TE_exon TE_EXON]
                    [-d EXON_DIFF]
```

Main outputs:

1. `${prefix}_TE_exon_anno.bed` (TE exons)
2. `${prefix}.TE.exon.anno.txt` (annotation for TE exons)
3. `${prefix}.TE.unit.anno.txt` (annotation for TE units)

## TERA quant

TERA quant is designed for teRNA quantification.

```text
usage: tera.py quant [-h] [-fq1 FASTQ1] [-fq2 FASTQ2] [--TE_gtf TE_GTF]
                     [-l LEVEL] [-s STRANDED_TYPE] [-o OUTPUT_DIR] [-p PREFIX]
                     [-r REF_GENOME] [-a ANNOTATION] [--TE_exon TE_EXON]
                     [-q QUANT] [-i INDEX] [-t NTHREAD]
```

Main outputs:

1. `${prefix}.transcript.quant.out`: all transcripts including TE and nonTE (transcript id, length, eff length, count, TPM)
2. `${prefix}.TE.exon.quant.out`: TE exon cluster quantification (exon cluster, count, TPM)
3. `${prefix}.TE.unit.quant.out`: TE unit quantification (TE ID, count)
4. `${prefix}.TE.family.quant.out`: TE family quantification (family ID, count)
