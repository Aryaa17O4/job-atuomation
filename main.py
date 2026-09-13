from workflow1.runner import collect, save_json

if __name__ == "__main__":
    jobs = collect()
    save_json(jobs, "jobs.json")
    print(f"Workflow 1 complete: {len(jobs)} unique jobs collected.")
