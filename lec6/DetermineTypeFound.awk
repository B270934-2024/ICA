cat nem.fasta| awk '{
BEGIN{FS="|";OFS=" ";}
if($1=">");
print{"Header"}
if($1!=">");
print{substr($1,1,1)} >"starter.txt"
}'
