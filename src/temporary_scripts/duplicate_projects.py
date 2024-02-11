from dominion_data import DominionData

if __name__ == "__main__":
    print("Queue Number,Latitute,Longitude,Queue Date,Substation Name,Substation Transformer,Capacity (MW),Interdependency Status")
    printed = set()

    data = DominionData()
    snames = sorted(data.get_substation_names())
    printers = {}
    for sname in snames:
        sub = data.get_substation(sname)
        groupings = sub.get_groupings()
        for grouping in groupings:
            y,q,t = grouping
            transf = sub.projects[grouping]
            dominants = transf.get_dominant_projects()
            if dominants:
                for qn,l in dominants:
                    # if qn in printed:
                    #     continue
                    if (y,q) not in printers:
                        printers[(y,q)] = []
                    printers[(y,q)].append(l)
                    printed.add(qn)
    
    for printer in sorted(printers.keys()):
        print(f"{printer}")
        print(f"{len(printers[printer])}")
        # for line in printers[printer]:
        #     print(line)