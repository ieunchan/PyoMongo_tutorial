def create_mongodb(name,age,resident,relationship):
    document = {"이름": f"{name}", "나이": f"{age}", "거주지": f"{resident}","관계": f"{relationship}"}
    return document