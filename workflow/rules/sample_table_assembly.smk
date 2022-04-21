rule sample_table_assembly:
    input:
        "results/texts/genome_IDs.txt"
    output:
        "config/pep/UHGG_human-gut-v2-0_genomes.csv"
    conda:
        "../envs/python_env.yaml"
    script:
        "../scripts/sample_table_assembly.py"