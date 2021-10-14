with open("description_definition.txt", "r") as file: 
    line = file.read().split("\n")

    gene = "attenuation"
    define_gene = "Attenuation"
    filename = "attenuation"

    define_gene_list = []
    for definition in line:
    	if gene in definition:
    		define_gene_list.append(define_gene)
    	else:
    		define_gene_list.append("None")

    f = open("define_gene_"+filename+".txt", "w")
    for line in define_gene_list:
        f.write(str(line))
        f.write("\n")
    f.close()