import json

def write_json (data, filename="sample.json"):
    with open (filename, "w") as f:
        json.dumps(data, f, indent=4)

with open("oracle/sample.json") as json_file:
    data = json.loads(json_file)
    temp = data["12201EE"]  #name of the container in which info is to be appended
    y = { "dbimgunenmd5sum": "new_numbers",
            "edition": "ee",
            "girollbackstr": "",
            "recommended_dbaastools_ver": "181103",
            "patchid": "34219654",
            "exapatchid": "34219654",
            "description_opatch": "OPatch patch of version 12.2.0.1.14 for Oracle software releases 12.1.0.x (installer) and 12.2.0.x (July 2022)",
            "patch_level": "12201_dbbp220719",
            "opatch": "/exadata_jul2022/p6880880_122010_Linux-x86-64.zip",
            "version": "12.2.0.1.220719",
            "dbimgmd5sum": "new_numbers",
            "patchmd5sum": "new_numbers",
            "type": "bundle",
            "apply_str": "",
            "ojvm": "/exadata_jul2022/p33829783_122010_Linux-x86-64.zip",
            "description": "DB 12.2.0.1.220719 DATABASE RELEASE UPDATE (Jul 2022)",
            "rbdbimage": "/exadata_apr2022/db12201_apr22.tar.gz.gpg",
            "dbaastoolsrpm": "/shome/dbaastools_exa.rpm",
            "required_dbaastools_ver": "181103",
            "opatchmd5sum": "08f34832b801436661b50f9bab35afbb",
            "date": "Mon 13 Jun 2022 00:22:41 AM PDT",
            "psuzip": "/exadata_jul2022/p34219654_122010_Linux-x86-64.zip",
            "rollback_reapply": "",
            "rollbackstr": "",
            "rollback_needed_before_apply": "23026585:datapatch:normal,26526726: :normal,26362821: :normal,26198926: :normal,26272761:datapatch:normal,25875415:datapatch:normal,29163642: :normal,28725094::normal,26124078: :normal",
            "oneoff": "",
            "bpdbimage": "/exadata_jul2022/db12201_jul22.tar.gz.gpg"
         }  #y refers to the key-value pairs
    temp.append(y)

write_json(data)
