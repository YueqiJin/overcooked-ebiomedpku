# Example

## Step-by-step commands

### 1. Detect TE-derived RNAs

```bash
TERA detect \
  -fq1 ${fastq1} \
  -fq2 ${fastq2} \
  --TE_bed ${ref_TE_bed} \
  --TE_gtf ${ref_TE_gtf} \
  -p ${prefix} \
  -r ${ref_genome_fasta} \
  -a ${ref_genome_gtf} \
  -t ${nthread}
```

### 2. Annotate TE-derived RNAs

```bash
TERA anno \
  -i ${TERA_detect_gtf} \
  --TE_exon ${TERA_detect_bed} \
  --TE_bed ${ref_TE_bed} \
  -p ${prefix} \
  -a ${ref_genome_gtf}
```

### 3. Quantify (exon level)

```bash
TERA quant \
  -fq1 ${fastq1} \
  -fq2 ${fastq2} \
  -l 1 \
  -q rsem \
  --TE_gtf ${TERA_detect_gtf} \
  --TE_exon ${TERA_anno_bed} \
  -p ${prefix} \
  -r ${ref_genome_fasta} \
  -a ${ref_genome_gtf} \
  -t ${nthread}
```

### 4. Quantify (unit and family levels)

```bash
TERA quant \
  -fq1 ${fastq1} \
  -fq2 ${fastq2} \
  -l 2 \
  --TE_gtf ${ref_TE_gtf} \
  -p ${prefix} \
  -r ${ref_genome_fasta} \
  -a ${ref_genome_gtf} \
  -t ${nthread}
```
