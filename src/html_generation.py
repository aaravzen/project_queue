from dominion_data import DominionData, Substation

class HtmlGenerator:
    def __init__(self) -> None:
        pass

    def create_page(self, title, body):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="initial-scale=1.0">
    <title>{title}</title>

    <link rel="stylesheet" href="styling/output.css">
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
    
    def create_substation_page(self, substation):
        return self.create_page(substation.name, self.get_substation_body(substation))


def victoria():
    data = DominionData()
    substations = data.get_substation_names()
    victoria_substation = data.get_substation("Victoria")
    
    htmlgen = HtmlGenerator()
    vp = htmlgen.create_substation_page(victoria_substation)
    print(vp)

def hanover():
    data = DominionData()
    substations = data.get_substation_names()
    print(substations)
    hanover_substation = data.get_substation("Hanover")
    
    htmlgen = HtmlGenerator()
    hp = htmlgen.create_substation_page(hanover_substation)
    print(hp)

def lanexa():
    data = DominionData()
    substations = data.get_substation_names()
    hanover_substation = data.get_substation("Lanexa")
    
    htmlgen = HtmlGenerator()
    hp = htmlgen.create_substation_page(hanover_substation)
    print(hp)

if __name__ == "__main__":
    # victoria()
    # hanover()
    lanexa()
