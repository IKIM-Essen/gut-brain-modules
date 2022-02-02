# An collection of Snakemake rules imported in the main Snakefile.
# Put all your rules an a Snakemake Module in this directory.



rule download_rule:
    output:
        "results/test/{sample}.gff.gz",
    log:
        "logs/test/{sample}.log",
    params:
        url = lambda wildcards: get_url_for_sample(wildcards) #url needs to equal the the ftp link string. so
    conda:
        "../envs/example.yaml"
    shell:
        "wget -nv -O {output} {params.url}" # needs to be ftp link string. 

