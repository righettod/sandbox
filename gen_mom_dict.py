# Dirty utility script to generate different fuzzing dictionaries to discover MOM items
# See https://www.ibm.com/docs/en/ibm-mq/9.0?topic=objects-rules-naming-mq
env_names = ["DEV", "TEST", "PROD", "STAGING", "UAT", "PREPROD",
             "BETA", "PRD", "STG", "TST", "STAGINGAREA", "STAGING-AREA", "QUAL", "TEMP"]
qm_prefixes = ["QM", "QMANAGER"]
entries = []
instance_count = 10
env_names.sort()
qm_prefixes.sort()
# Queue Managers - First approach
with open("qm1.txt", mode="w", encoding="utf-8") as f:
    entries.clear()
    for qm_prefix in qm_prefixes:
        v = f"{qm_prefix}"
        entries.append(v.upper())
        entries.append(v.lower())
        entries.append(v.capitalize())
        for i in range(instance_count):
            v = f"{qm_prefix}{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{qm_prefix}.{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{qm_prefix}_{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
    entries.sort()
    f.write("\n".join(entries))
# Queue Managers - Second approach
with open("qm2.txt", mode="w", encoding="utf-8") as f:
    entries.clear()
    with open("1-4_all_letters_a-z.txt", mode="r", encoding="utf-8") as f2:
        lines = f2.read().splitlines()
    for line in lines:
        if len(line) < 2:
            continue
        entries.append(line.lower())
        entries.append(line.upper())
        entries.append(line.capitalize())
        for i in range(instance_count):
            entries.append(f"{line.lower()}{i}")
            entries.append(f"{line.upper()}{i}")
            entries.append(f"{line.capitalize()}{i}")
            entries.append(f"{line.lower()}.{i}")
            entries.append(f"{line.upper()}.{i}")
            entries.append(f"{line.capitalize()}.{i}")
            entries.append(f"{line.lower()}_{i}")
            entries.append(f"{line.upper()}_{i}")
            entries.append(f"{line.capitalize()}_{i}")
    entries = list(set(entries))
    entries.sort()
    f.write("\n".join(entries))
# Queues
with open("q1.txt", mode="w", encoding="utf-8") as f:
    entries.clear()
    for env_name in env_names:
        v = f"{env_name}.QUEUE"
        entries.append(v.upper())
        entries.append(v.lower())
        entries.append(v.capitalize())
        v = f"{env_name}.DEAD.LETTER.QUEUE"
        entries.append(v.upper())
        entries.append(v.lower())
        v = f"{env_name}.BASE.TOPIC"
        entries.append(v.upper())
        entries.append(v.lower())
        entries.append(v.capitalize())
        v = f"{env_name}_QUEUE"
        entries.append(v.upper())
        entries.append(v.lower())
        entries.append(v.capitalize())
        v = f"{env_name}_DEAD_LETTER_QUEUE"
        entries.append(v.upper())
        entries.append(v.lower())
        v = f"{env_name}_BASE_TOPIC"
        entries.append(v.upper())
        entries.append(v.lower())
        entries.append(v.capitalize())
        for i in range(instance_count):
            v = f"{env_name}.QUEUE.{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}.DEAD.LETTER.QUEUE.{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}.BASE.TOPIC.{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_QUEUE_{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_DEAD_LETTER_QUEUE_{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_BASE_TOPIC_{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}.QUEUE{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}.DEAD.LETTER.QUEUE{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}.BASE.TOPIC{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_QUEUE_{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_DEAD_LETTER_QUEUE{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
            v = f"{env_name}_BASE_TOPIC{i}"
            entries.append(v.upper())
            entries.append(v.lower())
            entries.append(v.capitalize())
    entries = list(set(entries))
    entries.sort()
    f.write("\n".join(entries))
