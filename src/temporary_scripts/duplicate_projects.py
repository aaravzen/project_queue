from dominion_data import DominionData, Substation

if __name__ == "__main__":
    print("Queue Number,Latitute,Longitude,Queue Date,Substation Name,Substation Transformer,Capacity (MW),Interdependency Status")
    printed = set()

    data = DominionData()
    snames = sorted(data.get_substation_names())
    for sname in snames:
        sub = data.get_substation(sname)
        groupings = sub.get_groupings()
        for grouping in groupings:
            transf = sub.projects[grouping]
            dominants = transf.get_dominant_projects()
            if dominants:
                for qn,l in dominants:
                    if qn in printed:
                        continue
                    print(l)
                    printed.add(qn)
        # if printed:
        #     print("")