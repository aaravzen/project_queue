import os
import random
from dominion_data import DominionData, Substation

class HtmlGenerator:
    def __init__(self) -> None:
        self.generated_substations = {}

    def create_page(self, title, body):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="initial-scale=1.0">
    <title>{title}</title>

    <link rel="stylesheet" href="../styling/output.css">
</head>
<body class="bg-slate-800">
{body}
</body>
</html>"""
    
    def get_substation_quarter_label(self, quarter, start, span):
        y,q = quarter
        return f'<div class="bg-slate-700 text-purple-200 p-1 col-start-{start} col-span-{span} flex justify-center">{y} Q{q}</div>'
    
    def get_substation_transformer_label(self, transformer, start):
        return f'<div class="bg-slate-700 text-purple-200 p-1 col-start-{start} col-span-1 flex justify-center">{transformer}</div>'

    def get_substation_body_header(self, substation: Substation):
        quarters = substation.get_quarters()
        self.quarter_starts = {}
        self.yqTx_starts = {}

        quarter_row = []
        start = 2
        for q in quarters:
            quarter,transformers = q
            span = len(transformers)
            quarter_row.append(self.get_substation_quarter_label(quarter, start, span))
            self.quarter_starts[quarter] = start
            start += span
        quarter_row = "\n".join(x for x in quarter_row)

        transformer_row = []
        start = 2
        for q in quarters:
            quarter,transformers = q
            for t in transformers:
                transformer_row.append(self.get_substation_transformer_label(t, start))
                yqTx = (quarter[0], quarter[1], t)
                self.yqTx_starts[yqTx] = start
                start += 1
        transformer_row = "\n".join(x for x in transformer_row)

        return f"""{quarter_row}

{transformer_row}
"""
    
    def get_in_service(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-green-400 hover:bg-green-500">{label}In Service</div>'
    
    def get_in_construction(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-green-300 hover:bg-green-400">{label}In Construction</div>'
    
    def get_in_coop(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-green-200 hover:bg-green-300">{label}In Coop</div>'

    def get_project_a(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-purple-300 hover:bg-purple-400">{label}Project A</div>'
    
    def get_project_b(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-purple-200 hover:bg-purple-300">{label}Project B</div>'
    
    def get_subordinate(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-blue-200 hover:bg-blue-300">{label}Subordinate</div>'
    
    def get_cancelled(self, start, span, label=""):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-red-200 hover:bg-red-300">{label}Cancelled</div>'

    def get_box(self, box_type, start, span, label=""):
        if box_type == "In Service": return self.get_in_service(start, span, label)
        if box_type == "In Construction": return self.get_in_construction(start, span, label)
        if box_type == "In COOP": return self.get_in_coop(start, span, label)
        if box_type == "Project A": return self.get_project_a(start, span, label)
        if box_type == "Project B": return self.get_project_b(start, span, label)
        if box_type == "Subordinate": return self.get_subordinate(start, span, label)
        if box_type == "Cancelled": return self.get_cancelled(start, span, label)
        else: return f'<div class="p-1 sm:p-2 col-start-{start} col-span-{span} bg-amber-400 hover:bg-amber-500">{label}UNKNOWN</div>'

    def get_date_label(self, date, start):
        return f'<div class="p-1 sm:p-2 col-start-{start} col-span-1 text-green-200 text-xs text-right">{date}</div>'

    def get_substation_project(self, substation: Substation, queue_number):
        projects = substation.get_queue_number_summary(queue_number)
        boxes = []
        prev_box = None
        label = ""
        date = ""
        date_set = False
        for proj in projects:
            if not date_set:
                label = f"{proj.queue_number} ({proj.capacity} MW)"
                date = f"{proj.queue_date}"
            if proj.interdependency_status == prev_box:
                continue
            grouping = substation.project_grouping(proj)
            start = self.yqTx_starts[grouping]
            boxes.append((proj.interdependency_status, start))
            prev_box = proj.interdependency_status
        
        # print(f"Trying to get sub project for {label}")
        # print(f"Boxes {boxes}")
        date_start = boxes[0][1] - 1
        date_label = self.get_date_label(date, date_start)

        substation_view = []
        for idx,box in enumerate(boxes):
            box_type, start = box
            end = self.columns
            if idx+1 < len(boxes):
                end = boxes[idx+1][1]
            span = end - start
            if len(substation_view) == 0:
                substation_view.append(self.get_box(box_type, start, span, label))
            else:
                substation_view.append(self.get_box(box_type, start, span))
        
        # print(f"Sub View {substation_view}")
        substation_view = "\n".join(x for x in substation_view)

        return f"""{date_label}
{substation_view}"""

    def get_substation_projects(self, substation: Substation):
        queue_numbers = substation.get_ordered_queue_numbers()
        project_view = []
        for qn in queue_numbers:
            project_view.append(self.get_substation_project(substation, qn))
        project_view = "\n".join(p for p in project_view)
        return f"""
{project_view}
"""

    def get_substation_body(self, substation: Substation):
        self.columns = substation.get_columns()
        header = self.get_substation_body_header(substation)
        projects = self.get_substation_projects(substation)
        
        return f"""<div class="p-2 md:p-4 grid grid-cols-{self.columns}">
        
{header}

{projects}

</div>"""
    
    def get_index_link(self, url, label):
        colors = [
            "bg-amber-200 hover:bg-amber-400",
            "bg-sky-200 hover:bg-sky-400",
            "bg-emerald-200 hover:bg-emerald-400",
            "bg-violet-200 hover:bg-violet-400",
            "bg-rose-200 hover:bg-rose-400",
            "bg-red-200 hover:bg-red-400",
            "bg-orange-200 hover:bg-orange-400",
            "bg-lime-200 hover:bg-lime-400",
            "bg-green-200 hover:bg-green-400",
            "bg-teal-200 hover:bg-teal-400",
            "bg-cyan-200 hover:bg-cyan-400",
            "bg-blue-200 hover:bg-blue-400",
            "bg-indigo-200 hover:bg-indigo-400",
            "bg-fuchsia-200 hover:bg-fuchsia-400",
            "bg-pink-200 hover:bg-pink-400",
        ]
        color = random.choice(colors)
        return f'<a class="p-1 md:p-2 {color}" href="{url}">{label}</a>'

    def get_index_body(self):
        links = []
        for station in sorted(self.generated_substations.keys()):
            url = self.generated_substations[station]
            links.append(self.get_index_link(url, station))
        links = "\n".join(l for l in links)

        return f"""<div class="p-1 md:p-2">
<h1 class="text-xl text-amber-100">Dominion Fleet Virginia Substations</h1>
<div class="p-2 md:p-4 flex text-slate-700 gap-2 flex-wrap">
        
{links}
        
</div>
</div>"""
    
    def create_substation_page(self, substation):
        fn = substation.url()
        file_path = os.path.join("site/", fn)

        page = self.create_page(substation.name, self.get_substation_body(substation))
        with open(file_path, "w") as output_file:
            output_file.write(page)
        self.generated_substations[substation.name] = fn

    def create_index_page(self):
        file_path = "site/index.html"
        page = self.create_page("Dominion Fleet", self.get_index_body())
        with open(file_path, "w") as output_file:
            output_file.write(page)


def victoria():
    data = DominionData()
    substations = data.get_substation_names()
    victoria_substation = data.get_substation("Victoria")
    
    htmlgen = HtmlGenerator()
    vp = htmlgen.create_substation_page(victoria_substation)
    print(vp)

if __name__ == "__main__":
    # victoria()
    data = DominionData()
    snames = data.get_substation_names()
    htmlgen = HtmlGenerator()
    for sub_name in snames:
        sub = data.get_substation(sub_name)
        htmlgen.create_substation_page(sub)
    htmlgen.create_index_page()