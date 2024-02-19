# project_queue

An outline of steps taken to complete the project will be provided below, for context.

## Initial Development

### Data

The work for the data involved:
- aggregation,
- sanitization, and
- the creation of relevant data models for the visualization


First, I had to aggregate the data from different documents (with different formats). This meant basic data formatting and parsing.

Next, I had to sanitize data errors with the csvs provided. This included a few steps ranging in difficulty: correcting malformed and misnamed data, correlating projects that matched multiple substations over differing years, funneling mislabeled data into the correct groupings.

After getting and cleaning the data provided, I generated the data models utilized in the visualizations. This involves the calculation and creation of new data fields that aren't provided by the data; the data generated provides information about the projects, transformers, substations, and project queue.

### Design

Next, I had to generate the designs for the site. I don't want to get bogged down in the details, so I'll provide a very short summary of the process:
- Sketch the planned outputs (wireframing; pen and paper - this contributes to the data modeling step above, so it happens early)
- Generate a mock-up design in html. This provides a proof of concept, in terms of the organization/aesthetics of the project. The mock-ups of the design are then used to build templates for the final site pages.
- Templatization of the mock-up. This step takes the design of the site pages and sets them up to input the data from the first steps. The templates are currently simple and will expand based on the needs of the site users.

### DevOps

The last steps (of the first cycle) involve the nitty gritty of the development, so these are the tasks most typically associated with "software developers." It's worth saying that all the above steps are also code though - the data work is being done in Python, a shell, and VS Code; the Design work is being done in html/css, with the templatization achieved in Python.

Delivery of the project involves:
- Connecting the data with the design templates in order to generate the site
- Getting the site live and accessible (url generation, deploying, hosting, etc)

## Additional Work

After meeting with Ryan regarding the initial site iteration, he discussed immediate additions/modifications he'd like to see. For documentation (and organization), the asks are as follows. Ordering of tasks based on dependency hierarchy and priority (within relevant buckets).

### Data

- Generation of csvs for specific data inquiries
- Filtering and viewing fuel type
- Addition of data sources for statistic generation. (Also: the statistic calculations).
- Correlation of data based on Hexagon established standard, generation of overlapping substation data.

While browsing the initial iteration of the site, Ryan and Aarav noticed some data discrepencies in the visualizations. Per these observations, Aarav generated csvs of relevant data sets for Ryan's use (in `src/temporary_generations`). These include finding transformers with conflicting dominant projects (eg. `2 queue numbers marked "Project A" on the same Substation on the same Transformer`) and inconsistent dominant projects (ie. `a Transformer that has a "Project B" but no "Project A"`).

Ryan also provided additional data to incorporate into the visualizations, which need to be aggregated into the data models (in `src/data`).

### Visualizations

- Backdating visualization based on initial queue_date in first spreadsheet encounter.
- Sorting substation projects based on various aspects (main sort: Transformer-Date(-Priority). others: Transformer-Priority-Date, Transformer-Capacity-Date. maybe Substation-Date but idk if any non-Transformer views are actually useful)
- Modification of project box and labels as per handwritten drawings
- Generation of stats and sketch/mockup/template for stats visualizations (for Transformers and Substations)
- Fixing boxes for broken assumption of unchanging queue_number capacity.
- Index page additions (categorization based on number of projects, containing identified bad data, combined substations with overlapping data)

## Misc for the developer

### How to run

- `python3 html_generation.py` from `/src/` to generate html
- `npx tailwindcss -i ./src/styling/input.css -o ./src/styling/output.css --watch` running to regenerate CSS on html generation