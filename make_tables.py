#import chembl_downloader

#path= chembl_downloader.download_extract_sqlite(version='29')

import chembl_downloader

def export():
    file1 = open("sch.txt","r+")
    lines = file1.readlines()
    for line in lines:
        line = line.replace('\n',' ')
        line = line.strip()
        line = line.split(' ')
        table_id = line[0]
        #print(table_id)
        line.pop(0)
        #print(line)
        data1 = ""
        for j in line:
            data1 = data1 +j+", "
            #print(data1)
        sql = """ select {} from {}""".format(data1[:-2],table_id)
        print(sql)
        df = chembl_downloader.query(sql)
        df.to_csv(table_id+'.csv', sep='\t', index=False)

export()

exit()           
df = chembl_downloader.query(sql)
df.to_csv('temp.csv', sep='\t', index=False)

exit()
sql = """
SELECT
    MOLECULE_DICTIONARY.chembl_id,
    MOLECULE_DICTIONARY.pref_name
FROM MOLECULE_DICTIONARY
JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
WHERE molecule_dictionary.pref_name IS NOT NULL
LIMIT 5
"""