# Job Agent — Workflow 1

Workflow 1 is the **job discovery/collection layer**. It does not submit applications.
It collects jobs, normalizes them into one schema, and writes `agent/jobs.json`.

## Structure

```text
job-agent/
├── agent/
│   ├── main.py
│   └── workflow1/
│       ├── models.py
│       ├── registry.py
│       ├── runner.py
│       ├── utils.py
│       └── platforms/
│           ├── remoteok.py
│           ├── remotive.py
│           ├── himalayas.py
│           ├── weworkremotely.py
│           ├── jobspresso.py
│           ├── workingnomads.py
│           ├── github_jobs.py
│           ├── stack_overflow.py
│           ├── devto.py
│           ├── hiring_threads.py
│           ├── aicte.py
│           ├── internshala.py
│           ├── foundit.py
│           ├── indeed.py
│           └── simplify.py
├── .github/workflows/
│   ├── workflow1.yml
│   └── keepalive.yml
└── requirements.txt
```

## Important

Every source gets its own adapter file, but an adapter is only enabled for
an integration that is actually supported. Legacy/undocumented endpoints are
left as safe stubs instead of pretending they are working.

The next workflow can consume `jobs.json` and handle resume tailoring,
matching, application routing, and application tracking.
