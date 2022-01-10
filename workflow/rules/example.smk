# An collection of Snakemake rules imported in the main Snakefile.
# Put all your rules an a Snakemake Module in this directory.


rule test_rule:
    output:
        "results/test-{sample}-{url}.txt",
    log:
        "logs/test-{sample}-{url}.log",
    conda:
        "../envs/example.yaml"
    shell:
        "echo 'This is an example rule for sample {wildcards.sample} with url {wildcards.url}' > {output} 2> {log}"
