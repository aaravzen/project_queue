import csv
import os
from datetime import date


class Project:
    def sanitize_substation_name(self):
        if self.substation_name == "'s Creek": self.substation_name = "Twitty's Creek"
        if self.substation_name == "28 428": self.substation_name = "Correctional"
        if self.substation_name == "BOWERS HILL": self.substation_name = "Bowers Hill"
        if self.substation_name == "Bowers Hill": self.substation_name = "Bowers Hill"
        if self.substation_name == "Buchanan/Glasgow": self.substation_name = "Buchanan"
        if self.substation_name == "COOP": self.substation_name = "Waverly"
        if self.substation_name == "COOP Waverly": self.substation_name = "Waverly"
        if self.substation_name == "Central": self.substation_name = "Central"
        if self.substation_name == "Charles City Road": self.substation_name = "Charles City Road"
        if self.substation_name == "Chickahominy": self.substation_name = "Turner"
        if self.substation_name == "Colony": self.substation_name = "Colony"
        if self.substation_name == "Copeland Park": self.substation_name = "Copeland Park"
        if self.substation_name == "Covington": self.substation_name = "Covington"
        if self.substation_name == "DOOMS": self.substation_name = "Dooms"
        if self.substation_name == "Dahlgren": self.substation_name = "Dahlgren"
        if self.substation_name == "Dooms 115": self.substation_name = "Dooms"
        if self.substation_name == "Dooms 115 kV": self.substation_name = "Dooms"
        if self.substation_name == "Dooms 115KV": self.substation_name = "Dooms"
        if self.substation_name == "Dooms 115kv": self.substation_name = "Dooms"
        if self.substation_name == "Dozier": self.substation_name = "Dozier"
        if self.substation_name == "ELMONT": self.substation_name = "Elmont"
        if self.substation_name == "Eagle Rock": self.substation_name = "Eagle Rock"
        if self.substation_name == "Elmont": self.substation_name = "Elmont"
        if self.substation_name == "Farmille": self.substation_name = "Farmville"
        if self.substation_name == "Fisherville": self.substation_name = "Fishersville"
        if self.substation_name == "Flaggy Run": self.substation_name = "Flaggy Run"
        if self.substation_name == "Flat Creek": self.substation_name = "Crewe"
        if self.substation_name == "Franconia": self.substation_name = "Franconia"
        if self.substation_name == "GORDONSVILLE": self.substation_name = "Gordonsville"
        if self.substation_name == "Gainesville": self.substation_name = "Gainesville"
        if self.substation_name == "Gordsonville": self.substation_name = "Gordonsville"
        if self.substation_name == "Goshen": self.substation_name = "Goshen"
        if self.substation_name == "Hamilton": self.substation_name = "Hamilton"
        if self.substation_name == "Harbour View": self.substation_name = "Harbour View"
        if self.substation_name == "Harrisburg": self.substation_name = "Harrisonburg"
        if self.substation_name == "Harvell": self.substation_name = "Harvell"
        if self.substation_name == "Hull Street": self.substation_name = "Hull Street"
        if self.substation_name == "IDYLWOOD": self.substation_name = "Idylwood"
        if self.substation_name == "Idylwood": self.substation_name = "Idylwood"
        if self.substation_name == "In Coop": self.substation_name = "Oak Grove"
        if self.substation_name == "Ironbridge": self.substation_name = "Iron Bridge"
        if self.substation_name == "Jefferson St.": self.substation_name = "Jefferson St."
        if self.substation_name == "KINGS FORK": self.substation_name = "Kings Fork"
        if self.substation_name == "KInderton": self.substation_name = "Kinderton"
        if self.substation_name == "Keene Mill": self.substation_name = "Keene Mill"
        if self.substation_name == "Kingsmill": self.substation_name = "Kings Mill"
        if self.substation_name == "Lakeside": self.substation_name = "Lakeside"
        if self.substation_name == "Landstown": self.substation_name = "Landstown"
        if self.substation_name == "Lebanon": self.substation_name = "Lebanon"
        if self.substation_name == "Lebonan": self.substation_name = "Lebanon"
        if self.substation_name == "Light Foot": self.substation_name = "Lightfoot"
        if self.substation_name == "Line 2076": self.substation_name = "Line 2076"
        if self.substation_name == "Midlithian": self.substation_name = "Midlothian"
        if self.substation_name == "Milleville": self.substation_name = "Millville"
        if self.substation_name == "Millville": self.substation_name = "Millville"
        if self.substation_name == "Milothian": self.substation_name = "Midlothian"
        if self.substation_name == "Mountain Rd": self.substation_name = "Mountain Rd"
        if self.substation_name == "OAK GROVE": self.substation_name = "Oak Grove"
        if self.substation_name == "OCCOQUAN": self.substation_name = "Occoquan"
        if self.substation_name == "ORANGE": self.substation_name = "Orange"
        if self.substation_name == "Pleasant Hill": self.substation_name = "Pleasant Hill"
        if self.substation_name == "Rockbridge": self.substation_name = "Rockbridge"
        if self.substation_name == "Ruritan": self.substation_name = "Ruritan"
        if self.substation_name == "Shacklefords": self.substation_name = "Shackleford"
        if self.substation_name == "Shellhorn": self.substation_name = "Shellhorn"
        if self.substation_name == "Shellhorn Road": self.substation_name = "Shellhorn"
        if self.substation_name == "Skippers": self.substation_name = "Trego"
        if self.substation_name == "South HIll": self.substation_name = "South Hill"
        if self.substation_name == "South Norfolk Sub": self.substation_name = "South Norfolk"
        if self.substation_name == "Sterling Park": self.substation_name = "Sterling Park"
        if self.substation_name == "Stuart Draft": self.substation_name = "Stuarts Draft"
        if self.substation_name == "Suffolk Substation": self.substation_name = "Suffolk"
        if self.substation_name == "TURNER": self.substation_name = "Turner"
        if self.substation_name == "TWITTYS CREEK": self.substation_name = "Twitty's Creek"
        if self.substation_name == "TX #2": self.substation_name = "Turner"
        if self.substation_name == "Third St.": self.substation_name = "Third St."
        if self.substation_name == "Twelth": self.substation_name = "Twelfth Street"
        if self.substation_name == "Twittys Creek": self.substation_name = "Twitty's Creek"
        if self.substation_name == "Varina": self.substation_name = "Varina"
        if self.substation_name == "Verona": self.substation_name = "Verona"
        if self.substation_name == "WAXPOOL SUB": self.substation_name = "Waxpool"
        if self.substation_name == "Wakeman": self.substation_name = "Wakeman"
        if self.substation_name == "Walney": self.substation_name = "Walney"
        if self.substation_name == "Walthall": self.substation_name = "Walthall"
        if self.substation_name == "Wareenton": self.substation_name = "Warrenton"
        if self.substation_name == "Warsaw": self.substation_name = "Northern Neck"
        if self.substation_name == "Waynesboro": self.substation_name = "Waynesboro"
        if self.substation_name == "Weyers Cave": self.substation_name = "Weyers Cave"
        if self.substation_name == "Willard": self.substation_name = "Willard"
        if self.substation_name == "Willoughby": self.substation_name = "Willoughby"
        if self.substation_name == "Winchester": self.substation_name = "Winchester"
        if self.substation_name == "Winters Branch": self.substation_name = "Winters Branch"
        if self.substation_name == "chickahominy": self.substation_name = "Turner"
    
    def get_date(self, filename):
        arr = filename.split("_")
        self.year = int(arr[0])
        m = int(arr[1])
        if m < 4: self.quarter = 1
        elif m < 7: self.quarter = 2
        elif m < 10: self.quarter = 3
        else: self.quarter = 4

    def __init__(self, queue_number, lat, long, fuel_type, capacity, substation_name, transformer, circuit, queue_date, status, status_code, interdependency_status, ia_executed, filename):
        self.queue_number = queue_number
        self.lat = lat
        self.long = long
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.substation_name = substation_name
        self.transformer = transformer.replace(" ", "")
        self.circuit = circuit
        self.queue_date = queue_date
        self.status = status
        self.status_code = status_code
        self.interdependency_status = interdependency_status
        self.ia_executed = ia_executed
        self.get_date(filename)

        self.sanitize_substation_name()
    
    def __repr__(self):
        return f"[Project {self.queue_number} ({self.status_code}) - {self.capacity}@T{self.transformer}@S{self.substation_name}]"

class Transformer:
    def __init__(self, name, year, quarter) -> None:
        self.name = name
        self.year = year
        self.quarter = quarter
        self.projects = []
    
    def add_project(self, project: Project):
        self.projects.append(project)
    
    def get_projects(self):
        return self.projects
    
    def get_project(self, queue_number):
        for proj in self.projects:
            if proj.queue_number == queue_number:
                return proj
        return None

class Substation:
    def __init__(self, name) -> None:
        self.name = name
        self.projects = {}
    
    def calculate(self):
        self.qToTXs = {}
        for grouping in self.projects.keys():
            year, quarter, tx = grouping
            q = (year,quarter)
            if q not in self.qToTXs:
                self.qToTXs[q] = set()
            self.qToTXs[q].add(tx)
    
    def project_grouping(self, project: Project):
        return (project.year, project.quarter, project.transformer)
    
    def add_project(self, project: Project):
        grouping = self.project_grouping(project)
        if grouping not in self.projects:
            year, quarter, name = grouping
            self.projects[grouping] = Transformer(name, year, quarter)
        self.projects[grouping].add_project(project)
        self.calculate()
    
    def get_columns(self):
        return len(self.projects) + 2

    def get_quarters(self):
        ret = []
        for q in sorted(self.qToTXs.keys()):
            ret.append((q, sorted(self.qToTXs[q])))
        return ret
    
    def get_groupings(self):
        ret = []
        for quarter,transformers in self.get_quarters():
            y,q = quarter
            for t in transformers:
                grouping = (y,q,t)
                ret.append(grouping)
        return ret

    def get_groupings_by_transformer(self):
        ret = self.get_groupings()
        ret.sort(key=lambda g: (g[2], g[0], g[1]))
        return ret

    def get_ordered_queue_numbers(self):
        ret = []
        added = set()

        rounds = ["In Service", "In Construction", "In COOP", "Project A", "Project B", "Subordinate", "Cancelled"]

        for round in rounds:
            for grouping in self.get_groupings_by_transformer():
                transf = self.projects[grouping]
                for proj in transf.get_projects():
                    if proj.interdependency_status == round and proj.queue_number not in added:
                        added.add(proj.queue_number)
                        ret.append(proj.queue_number)
        return ret
    
    def get_queue_number_summary(self, queue_number):
        ret = []
        for grouping in self.get_groupings():
            transf = self.projects[grouping]
            proj = transf.get_project(queue_number)
            if proj:
                ret.append(proj)
        return ret

class DominionData:
    def __init__(self):
        file_names = [
            "2021_06_30.csv",
            "2022_01_31.csv",
            "2022_05_01.csv",
            "2022_07_29.csv",
            "2022_10_31.csv",
            "2023_01_31.csv",
            "2023_04_28.csv",
            "2023_07_28.csv",
            "2023_10_30.csv",
            "2024_01_31.csv"
        ]
        
        self.substations = {}
        for fn in file_names:
            file_path = os.path.join("data/", fn)
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                for p in reader:
                    if p["Queue No"].strip() == "" or p["Substation Name"].strip() == "":
                        continue
                    proj = Project(
                        p["Queue No"],
                        p["Location (Latitude)"],
                        p["Location (Longitude)"],
                        p["Fuel Type"],
                        p["Capacity (MW)"],
                        p["Substation Name"],
                        p["Substation Transformer"],
                        p["Circuit"],
                        p["Date Queue Number Assigned"],
                        p["Status Description"],
                        p["Status"],
                        p["Interdependency Status"],
                        p["IA Executed (A)"],
                        fn
                    )

                    if proj.substation_name not in self.substations:
                        self.substations[proj.substation_name] = Substation(proj.substation_name)
                    self.substations[proj.substation_name].add_project(proj)
    
    def get_substation_names(self):
        return list(self.substations.keys())
    
    def get_substation(self, substation_name):
        return self.substations[substation_name]
                    