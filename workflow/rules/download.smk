#Download from a csv file, containing sample name and download url

rule download_rule:
    output:
        "results/test/{sample}.gff.gz",
    log:
        "logs/test/{sample}.log",
    params:
        url = lambda wildcards: get_url_for_sample(wildcards) 
    conda:
        "../envs/example.yaml"
    shell:
        "wget -nv -O {output} {params.url}"

