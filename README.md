# project_queue

An outline of steps taken to complete the project will be provided below, for context.

## Data

The work for the data involved:
- aggregation,
- sanitization, and
- the creation of relevant data models for the visualization

First, I had to aggregate the data from different documents (with different formats). This meant basic data formatting and parsing.

Next, I had to sanitize data errors with the csvs provided. This included a few steps ranging in difficulty: correcting malformed and misnamed data, correlating projects that matched multiple substations over differing years, funneling mislabeled data into the correct groupings.

After getting and cleaning the data provided, I generated the data models utilized in the visualizations. This involves the calculation and creation of new data fields that aren't provided by the data; the data generated provides information about the projects, transformers, substations, and project queue.

## Design

Next, I had to generate the designs for the site. I don't want to get bogged down in the details, so I'll provide a very short summary of the process:
- Sketch the planned outputs (wireframing; pen and paper - this contributes to the data modeling step above, so it happens early)
- Generate a mock-up design in html. This provides a proof of concept, in terms of the organization/aesthetics of the project. The mock-ups of the design are then used to
- Generate the templatization of the mock-up. This step takes the design of the site pages and sets them up to input the data from the first steps.

## DevOps

The last steps involve the nitty gritty of the development, so these are the tasks most typically associated with "software developers." It's worth saying that all the above steps are also code though - the data work is being done in Python, a shell, and VS Code; the Design work is being done in html/css, with the templatization achieved in Python.

Delivery of the project involves:
- Connecting the data with the design templates in order to generate the site
- Getting the site live and accessible (url generation, deploying, hosting, etc)

## Misc for the developer

### How to run

- `python3 html_generation.py` from `/src/` to generate html
- `npx tailwindcss -i ./src/styling/input.css -o ./src/styling/output.css --watch` running to regenerate CSS on html generation