# Example

## Step-by-step commands

### 1. Predict TSS with the deep-learning model

```bash
TEIRI_correct.py \
  --input sample \
  --short_path /abs/path/to/input \
  --chr_len /abs/path/to/chr.len \
  --window_length 10000 \
  -g /abs/path/to/reference.fa \
  -m /abs/path/to/model.pth \
  -p Deep-TEIRI
```

### 2. Merge TE-initiated transcripts across samples

```bash
TEIRI_merge.py \
  -i /abs/path/to/gtf.list \
  -r /abs/path/to/reference.gtf \
  --TE_anno /abs/path/to/TE.bed \
  --tss_window 50 \
  --max_tss 1 \
  --threshold 1 \
  -p Deep-TEIRI
```

### 3. Consolidate transcript annotations

```bash
TEIRI_consolidate.py \
  -i /abs/path/to/condition_gtf.list \
  -r /abs/path/to/reference.gtf \
  --TE_anno /abs/path/to/TE.bed \
  --tss_merge_distance 50 \
  --min_exon_length 20 \
  -p Deep-TEIRI
```

## Notes

- Use absolute paths for all inputs.
- Replace placeholder filenames with your dataset-specific files.
