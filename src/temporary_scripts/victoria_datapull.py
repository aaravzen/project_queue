'''
        visited = {}


                    if proj.substation_name == "Victoria":
                        if proj.queue_number in visited:
                            if visited[proj.queue_number] == proj.interdependency_status:
                                print(f"repeat {proj.queue_number}")
                            else:
                                print(f"change {proj.queue_number} to {proj.interdependency_status}")
                                visited[proj.queue_number] = proj.interdependency_status
                        else:
                            print(f"{proj.queue_number}: {proj.interdependency_status} ({proj.capacity})")
                            visited[proj.queue_number] = proj.interdependency_status

'''