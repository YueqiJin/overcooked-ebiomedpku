# Usage

## Command overview

```bash
circfull <command> [options]
```

Supported commands:

- `RG`: Reference-guided detection
- `DNSC`: De novo self-correction to consensus sequence
- `cRG`: Reference-guided detection using DNSC-corrected reads
- `strand`: Identify transcript strand of circFL-seq reads
- `sRG`: Reference-guided detection with stranded reads
- `mRG`: Merge circRNA results from RG and cRG/sRG
- `anno`: Annotate full-length circRNAs
- `geneExp`: Quantify gene expression to evaluate linear RNA residuals
- `var`: Call variants in circRNAs

## Common workflow

### Inputs

```bash
rawFq=M1.example.fq
cleanFq=M1.clean.fq
gtfFile=gencode.v19.annotation.sort.gtf.gz
genome=hg19.fa
thread=80
outDir=circFL_example
```

### 1. Trim/split raw reads

```bash
porechop-runner.py -t $thread -i $rawFq -o $cleanFq --barcode_threshold 95 --check_reads 1000
```

### 2. Detect full-length circRNA from clean reads (RG)

```bash
circfull RG -f $cleanFq -g $genome -a $gtfFile -t $thread -o $outDir
```

### 3. Identify strand information

```bash
circfull strand -f $rawFq -F $cleanFq -a $gtfFile -l 100 -t $thread -r $outDir -o $outDir
```

### 4. Detect from stranded reads (sRG)

```bash
circfull sRG -g $genome -a $gtfFile -s $outDir -t $thread -o $outDir
```

### 5. Build consensus with DNSC

```bash
circfull DNSC -f $cleanFq -t $thread -o $outDir
circfull DNSC -f $cleanFq -t $thread -o $outDir -c
```

### 6. Detect from DNSC consensus (cRG)

```bash
circfull cRG -f $outDir -g $genome -a $gtfFile -t $thread -o $outDir
```

### 7. Merge and filter circRNAs (mRG)

```bash
rmsk=rmsk.bed.gz
circfull mRG -f $cleanFq -g $genome -r $outDir -c $outDir -s $outDir -t $thread -o $outDir
```

### 8. Annotate full-length circRNAs

```bash
circfull anno -b ${outDir}/mRG/circFL_Normal_pass.bed -a $gtfFile -o ${outDir}/mRG/circFL_Normal_pass_anno.txt
```

### 9. Quantify gene expression

```bash
umgtfFile=gencode.v19.annotation.gtf
gene_ref=ref_gene.fa
createGeneRef $umgtfFile $genome $gene_ref
circfull geneExp -f $cleanFq -r $gene_ref -o $outDir -t $thread
```

### 10. Call variants

```bash
circfull var -f $cleanFq -g $genome -r $outDir -t $thread -o $outDir
```

## Key command options

### RG

```text
circfull RG -f fastq -g genome -a anno [-u] [-t threads] [-r] [-o output]
```

### DNSC

```text
circfull DNSC -f fastq [-t threads] [-c] [-m mem] [-o output]
```

### cRG

```text
circfull cRG -f DNSC -g genome -a anno [-t threads] [-u] [-o output]
```

### strand

```text
circfull strand -f fastq -F fastq2 -a anno [-r RG_dir] [-l hang_len] [-t threads] [-o output]
```

### sRG

```text
circfull sRG -g genome -a anno [-s strandDir] [-t threads] [-r] [-o output]
```

### mRG

```text
circfull mRG -f fastq -g genome [-r RG] [-c cRG] [-s sRG] [-t threads] [-o output]
```

### anno

```text
circfull anno -b bed -a anno [-o output]
```

### geneExp

```text
circfull geneExp -f fastq -r ref [-t threads] [-o output]
```

### var

```text
circfull var -f fastq -g genome [-r RG_dir] [-t threads] [-o output]
```

Note: Higher thread counts increase memory usage.
