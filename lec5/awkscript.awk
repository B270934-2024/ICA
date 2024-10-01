#!/usr/bin/awk -f
BEGIN{
FS="\t";OFS="_";
}
{
count++;
if($1 != "#");
{print "Currently counting "count;
total=total+($12*$3);
}
}
END{print "The total for "count" lines was " int(total) > "awkOutput.txt";
print "Script Complete" >> "awkOutput.txt";
print "Script Complete";
system("ls -alrt *awk*")
}
