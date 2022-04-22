rule convert_GBMs:
    input:
        GBMs="results/files/GBMs_in_Microorganisms.json",
        combinations="results/files/GBM_combinations.json",
    output:
        "results/files/GBMs_in_Microorganisms_final.json",
        "results/tables/GBMs_in_Microorganisms_final.csv",
    conda:
        "../envs/python_env.yaml"
    script:
        "../scripts/snakemake_scripts/final_GBMs.py"
