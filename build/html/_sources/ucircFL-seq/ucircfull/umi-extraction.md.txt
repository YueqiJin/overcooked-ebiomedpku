# UMI extraction

```bash
Usage: ucircfull extract_umi [--help] [--version] --input FQ --anchorx SEQ --umi SEQ [--noumi] --outdir DIR --prefix PREFIX --thread INT [--seqkit PATH] [--porechop PATH]

Extract UMI sequence and identify strand from ucircFL-seq raw fastq

Optional arguments:
  -h, --help            shows help message and exits
  -v, --version         prints version information and exits
  -i, --input FQ        ucircFL-seq raw fastq file. [required]
  -x, --anchorx SEQ     anchor sequence used in 1st strand cDNA synthesis. [required]
  -u, --umi SEQ         umi pattern. [default: "CTCNNNYRNNNYRNNNYRNNNGAG"]
  -n, --noumi           no UMIs were added to 1st strand anchor.
  -o, --outdir DIR      output directory. [default: "."]
  -p, --prefix PREFIX   output prefix. [default: "circFL"]
  -t, --thread INT      number of threads used. [default: 4]
  --seqkit PATH         path to seqkit. [default: "seqkit"]
  --porechop PATH       path to porechop. [default: "porechop"]
  --debug               enable debug output.
```

For ucircFL-seq data in default library preparation data (`$rawfastq`), run:

```bash
ucircfull extract_umi -i $rawfastq -x CTACACGACGCTCTTCCGATCT -o . -p $sample -t $thread
```

## Output

- `$sample`_strand.fastq
- `$sample`_umi.fasta
