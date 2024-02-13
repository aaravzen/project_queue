from dominion_data import DominionData

def get_and_print_duplicates():
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
            dominants = transf.get_duplicate_dominant_projects()
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

def get_and_print_proj_b_with_no_proj_a():
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
            proj_as = transf.get_proj_as()
            proj_bs = transf.get_proj_bs()
            # if sname == "Reedy Creek":
            #     print("REEDY CREEK")
            #     print(proj_as)
            #     print(proj_bs)
            if proj_bs and not proj_as:
                # if sname == "Reedy Creek":
                #     print("got to the inner")
                for qn,l in proj_bs:
                    # if qn in printed:
                    #     continue
                    # 
                    # why the fuck is this clashing
                    # shouldn't I be able to uncomment 
                    if (y,q) not in printers:
                        printers[(y,q)] = []
                    printers[(y,q)].append(l)
                    printed.add(qn)
    
    for printer in sorted(printers.keys()):
        # print(f"{printer}")
        # print(f"{len(printers[printer])}")
        if printer == (2024, 1):
            for line in printers[printer]:
                print(line)

def print_proj(queue_number):
    data = DominionData()
    snames = sorted(data.get_substation_names())
    printers = {}
    for sname in snames:
        sub = data.get_substation(sname)
        groupings = sub.get_groupings()
        for grouping in groupings:
            y,q,t = grouping
            transf = sub.projects[grouping]
            proj = transf.get_project(queue_number)
            if proj:
                print(f'{y}Q{q}: {proj}')


if __name__ == "__main__":
    # get_and_print_duplicates()
    # get_and_print_proj_b_with_no_proj_a()
    print_proj("VA22044")