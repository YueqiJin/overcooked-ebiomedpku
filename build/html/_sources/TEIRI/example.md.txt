# Example

## Step-by-step commands

### 1. Correct TSS of first exons

```bash
TEIRI_correct.py \
  -i /abs/path/gtf.list \
  -r /abs/path/reference.gtf \
  -l /abs/path/flair.corrected.bed12 \
  -c /abs/path/tss_score.tsv \
  --TE_anno /abs/path/TE.bed \
  --eRNA_anno /abs/path/eRNA.bed \
  -p TEIRI
```

### 2. Merge TE-initiated transcripts in one condition

```bash
TEIRI_merge.py \
  -i /abs/path/gtf.list \
  -r /abs/path/reference.gtf \
  -l /abs/path/flair.corrected.bed12 \
  --corrected_tss /abs/path/TEIRI.corrected_tss.tsv \
  -p TEIRI
```

### 3. Consolidate transcripts across conditions

```bash
TEIRI_consolidate.py \
  -i /abs/path/condition_gtf.list \
  -r /abs/path/reference.gtf \
  --TE_anno /abs/path/TE.bed \
  -p TEIRI
```

## Notes

- Use absolute paths for all input files.
- Upstream README does not provide a complete shell script example, so the commands above are a practical template based on documented CLI options.
