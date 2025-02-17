import json

# Leer el archivo original
with open("/root/cuda-ilab/datasets/skills_train_msgs_2025-02-17T11_12_55.jsonl", "r", encoding="utf-8") as f_in:
    lines = f_in.readlines()

# Escribir el archivo corregido
with open("/root/cuda-ilab/datasets/output.jsonl", "w", encoding="utf-8") as f_out:
    for line in lines:
        data = json.loads(line)
        json_line = json.dumps(data, ensure_ascii=False, indent=None)
        f_out.write(json_line + "\n")
