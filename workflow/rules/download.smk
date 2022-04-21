#Download from a csv file, containing sample name and download url

rule download_rule:
    output:
        temp("results/genomes/gff_files/{sample}.gff"),
    threads: 8
    log:
        "logs/test/{sample}.log",
    params:
        url = lambda wildcards: get_url_for_sample(wildcards) 
    conda:
        "../envs/example.yaml"
    shell:
        "wget -nv -O {output} {params.url}"

