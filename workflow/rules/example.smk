# Test rule, showcasing how Snakemake works


rule test_rule:
    output:
        "results/test-{sample}-{url}.txt",
    log:
        "logs/test-{sample}-{url}.log",
    conda:
        "../envs/example.yaml"
    shell:
        "echo 'This is an example rule for sample {wildcards.sample} with url {wildcards.url}' > {output} 2> {log}"
