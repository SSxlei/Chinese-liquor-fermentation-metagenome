#!/bin/bash
#SBATCH -c 16
#SBATCH --mem=100G
concat () {
/public/home/wuq8022600160/anaconda3/envs/antismash7/bin/antismash 11.GTDB_tk/rename/ACT/${1}.fa --taxon bacteria --output-dir 13.antismash/${1} --genefinding-tool prodigal --cb-knownclusters -c 4 --cc-mibig --cb-general --cb-subclusters --fullhmmer
}
export -f concat
cat binid600|parallel -j 4 concat {}