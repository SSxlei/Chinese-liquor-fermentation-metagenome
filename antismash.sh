#!/bin/bash
#SBATCH -c 16
#SBATCH --mem=100G
for i in $(cat sample_id1); do
/public/home/wuq8022600160/anaconda3/envs/xl/antismash6.0/bin/antismash 03.Assembly-metaspades/ACT/${i}.fasta --taxon bacteria --output-dir antismash/${i} --genefinding-tool prodigal --cb-knownclusters -c 16 --cc-mibig --cb-general
done