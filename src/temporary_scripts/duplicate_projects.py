from dominion_data import DominionData, Substation

if __name__ == "__main__":
    data = DominionData()
    snames = sorted(data.get_substation_names())
    for sname in snames:
        printed = False
        sub = data.get_substation(sname)
        groupings = sub.get_groupings()
        for grouping in groupings:
            transf = sub.projects[grouping]
            if transf.has_multiple_dominant_projects():
                printed = True
        if printed:
            print("")