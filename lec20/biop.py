#!/bin/python3
def meanseqs(typ="COX1",grup="Mammalia",ret="20"):
    import sys
    from Bio.Seq import Seq
    from Bio import Entrez,SeqIO
    Entrez.email = "s2761220@ed.ac.uk"
    query=typ+" "+grup+" complete"
    sear=Entrez.esearch(db="protein",term=query,retmax=ret)
    result=Entrez.read(sear)
    print(result.keys())
    count=0
    totlen=0
    print("There were " + result['Count'] + " results")
    for entry in result["IdList"]:
        entfile=Entrez.efetch(db="protein",id=entry,rettype="gb")
        record=SeqIO.read(entfile,"genbank")
        print(record.id+"\t"+record.description+"\t"+record.seq[0:10])
        count+=1
        totlen+=len(record.seq)
        if count == 20:
            break
    mean=totlen / count
    return mean
def downloadsequences(typ="COX1",grup="Mammalia",ret="20"):
    import sys
    from Bio.Seq import Seq
    from Bio import Entrez,SeqIO
    Entrez.email = "s2761220@ed.ac.uk"
    query=typ+" "+grup+" complete"
    sear=Entrez.esearch(db="protein",term=query,retmax=ret)
    res=Entrez.read(sear)
    all_fastas=open("all_fastas.faa","w")
    s=Entrez.efetch(db="protein",id=res['IdList'],retmode="text",rettype="fasta")
    sa=s.read()
    all_fastas.write(sa)
    all_fastas.close()
    return print(str(open("all_fastas.faa").read().count(">")) + " sequences downloaded")

print("Average length of the counted proteins: "+str(meanseqs("COXI","Mammalia","10")))
downloadsequences("COX1","Mammalia","3")
