'''

        station_count = {}
        projects = []

        

            stations = set()


            
                    projects.append(proj)
                    stations.add(proj.substation_name)

                    


            for station in stations:
                if station not in station_count:
                    station_count[station] = 0
                station_count[station] += 1

                

        good = 0
        gs = set()
        for station in sorted(station_count):
            if station_count[station] < len(file_names):
                # print(f"{station} - {station_count[station]}")
                pass
            else:
                good += 1
                gs.add(station)

        # data validation -> check for projects in multiple queues
        # move to good queue if other is malformed or incomplete.
        # overlap remains between the following ~good substations:
        # Sinai/South Boston
        # Buchanan/Glasgow
        # Watkins Corner/Franklin
        # Oak Grove/Waverly (In Coop/Coop/etc)
        # Gordonsville/Somerset
        projToGood = {}
        for proj in projects:
            if proj.substation_name in gs:
                projToGood[proj.queue_number] = proj.substation_name
        
        for proj in projects:
            if proj.queue_number in projToGood and projToGood[proj.queue_number] != proj.substation_name:
                #print(f"queue number {proj.queue_number} matches good {projToGood[proj.queue_number]} as well as {proj.substation_name}")
                pass

'''