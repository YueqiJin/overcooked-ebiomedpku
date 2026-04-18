# UMI clustering

```bash
Usage: ucircfull clust_umi [--help] [--version] --input FQ --umi FA [--seq VAR] --outdir DIR --prefix PREFIX --thread INT [--seqkit PATH]

UMI clusting guided consensus generation.

Optional arguments:
  -h, --help            shows help message and exits
  -v, --version         prints version information and exits
  -i, --input FQ        stranded fastq file. [required]
  -u, --umi FA          umi fasta file. [required]
  -s, --seq             generate sequence cluster. [default: false]
  -o, --outdir DIR      output directory. [default: "."]
  -p, --prefix PREFIX   output prefix. [default: "circFL"]
  -t, --thread INT      number of threads used. [default: 4]
  --seqkit PATH         path to seqkit. [default: "seqkit"]
```

```bash
ucircfull clust_umi -i ${sample}_strand.fastq -u ${sample}_umi.fasta -o . -p $sample -t $thread
```

## Output

- `$sample`_umi.clstr: UMI clustering result
- `$sample`_seq.clstr (optional): sequence clustering result
