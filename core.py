import json
import os

def extract(json_path,out_path):
    """
    :param json_file: /public/home/wuq8022600160/xulei/metagenome/hmn_fj/hong_6samples_metagenomic/antismash/jsonfile
    :param out_path: /public/home/wuq8022600160/xulei/metagenome/hmn_fj/hong_6samples_metagenomic/antismash
    """

    json_files=os.listdir(json_path)

    isExists = os.path.exists(out_path)
    if not isExists:
        out_dir=os.mkdir(out_path)
    file_error = open("error_log.txt", "w+")
    for json_file in json_files:
        try:
            if json_file[-4:]=="json":
                file=open(json_path+json_file)
                lines = [line.strip('\n') for line in file.readlines()]
                file.close()

                string="".join(lines)
                root=json.loads(string)

                records=root['records']

                timings=list(dict.keys(root["timings"]))
                # print(timings)


                file_w=open(out_path+json_file[:-5]+".faa","w+")

                for record in  records:
                    record_id=record["id"]

                    if record_id in timings:
                        features=record["features"]

                        for feature in features:
                            qualifiers=feature["qualifiers"]

                            if "gene_kind" in qualifiers.keys() and \
                                    qualifiers["gene_kind"]==["biosynthetic"]:

                                loc=feature["location"]
                                # print(loc)
                                AA_seq=qualifiers["translation"][0]
                                # print(AA_seq)

                                string_head=">"+record_id + "|"+loc
                                file_w.write(string_head+"\n")
                                file_w.write(AA_seq+"\n")
                file_w.close()
        except:
                file_error = open("error_log.txt", "w+")
                file_error.write(json_file)

def main():
    extract("/public/home/wuq8022600160/xulei/metagenome/hmn_fj/hong_6samples_metagenomic/antismash/jsonfile/","out_path/")

if __name__ == '__main__':
    main()
