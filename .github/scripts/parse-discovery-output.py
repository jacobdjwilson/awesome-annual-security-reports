import os

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}={value}\n")

def main():
    log_file = "discovery_output.log"
    data = {}
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            for line in f:
                if "=" in line:
                    parts = line.strip().split("=", 1)
                    if parts[0].startswith("DISCOVERY_"):
                        data[parts[0]] = parts[1]

    def parse(key):
        return data.get(key, "0")

    write_output("tasks", parse("DISCOVERY_TASKS"))
    write_output("created", parse("DISCOVERY_CREATED"))
    write_output("suppressed", parse("DISCOVERY_SUPPRESSED"))
    write_output("skipped", parse("DISCOVERY_SKIPPED"))
    write_output("pdf_finds", parse("DISCOVERY_PDF_FINDS"))
    write_output("landing_finds", parse("DISCOVERY_LANDING_FINDS"))
    write_output("tier_current", parse("DISCOVERY_TIER_CURRENT"))
    write_output("tier_stale", parse("DISCOVERY_TIER_STALE"))
    write_output("tier_old", parse("DISCOVERY_TIER_OLD"))
    write_output("vt_clean", parse("DISCOVERY_VT_CLEAN"))
    write_output("vt_suspicious", parse("DISCOVERY_VT_SUSPICIOUS"))
    write_output("vt_malicious", parse("DISCOVERY_VT_MALICIOUS"))

    exit_code = os.environ.get("EXIT_CODE", "0")
    write_output("exit_code", exit_code)

if __name__ == "__main__":
    main()
