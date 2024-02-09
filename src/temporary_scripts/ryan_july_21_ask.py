'''
                    if fn == "2024_01_31.csv":
                        if proj.interdependency_status == "Project A" or proj.interdependency_status == "Project B":
                            qd = proj.queue_date
                            m,d,y = qd.split("/")
                            y = int(y)
                            m = int(m)
                            if y <= 21 and m <= 7:
                                print(f'{proj.queue_number} at latlong ({proj.lat}, {proj.long}) has been {proj.interdependency_status} since {proj.queue_date}')
                            elif y < 21:
                                print(f'{proj.queue_number} at latlong ({proj.lat}, {proj.long}) has been {proj.interdependency_status} since {proj.queue_date}')
'''