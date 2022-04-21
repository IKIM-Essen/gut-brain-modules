rule get_GBMs_in_microorganism:
    input:
        gff_files = lambda wildcards: expand(
            "results/genomes/gff_files/{sample}.gff",
            sample = get_samples(),
        ),
        combinations = "results/files/GBM_combinations.json",
        sample_table = "config/pep/UHGG_human-gut-v2-0_genomes.csv"
    output:
        "results/files/GBMs_in_Microorganisms.json"
    threads: 8
    params:
        samples = get_samples()
    conda:
        "../envs/python_env.yaml"
    script:
        "../scripts/snakemake_scripts/download.py"