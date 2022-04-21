rule get_genome_IDs:
    output:
        "results/texts/{page_ID}.txt"
    conda:
        "../envs/python_env.yaml"
    script:
        "../scripts/IDs_per_page.py"
