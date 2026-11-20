import json, os, re, subprocess, sys
from pathlib import Path

count = int(sys.argv[1]) if len(sys.argv) > 1 else 15
worktrees = [line.split(" ", 1)[1] for line in subprocess.run(
    ["git", "worktree", "list", "--porcelain"], capture_output=True, text=True, check=True
).stdout.splitlines() if line.startswith("worktree ")]
projects = Path(os.environ.get("CLAUDE_CONFIG_DIR", Path.home() / ".claude")) / "projects"
sessions = sorted(
    (f for w in worktrees for f in (projects / re.sub(r"[^A-Za-z0-9]", "-", w)).glob("*.jsonl")
     if f.stat().st_size > 50_000),
    key=lambda f: f.stat().st_mtime, reverse=True,
)[1:count + 1]

def text_of(content):
    if isinstance(content, str): return content
    return "\n".join(c.get("text", "") for c in content if c.get("type") == "text")

def clean(text):
    text = re.sub(r"<(system-reminder|t3_context)\b.*?</\1>", "", text, flags=re.S)
    return re.sub(r"<local-command-stdout>.*?</local-command-stdout>", "", text, flags=re.S).strip()

def truncate(text, limit):
    return text if len(text) <= limit else f"{text[:limit // 2]} […] {text[-limit // 2:]}"

for session in sessions:
    last_reply, tools, header = "", 0, None
    for line in session.open():
        entry = json.loads(line)
        if entry.get("isSidechain"): continue
        if header is None and entry.get("cwd"): header = f"# {session.name} {entry['cwd']} {entry.get('gitBranch')}"
        message = entry.get("message") or {}
        content = message.get("content")
        if entry.get("type") == "assistant" and isinstance(content, list):
            for part in content:
                if part.get("type") == "text" and part["text"].strip(): last_reply = part["text"].strip()
                elif part.get("type") == "tool_use": tools += 1
        elif entry.get("type") == "user" and not entry.get("isMeta") and not entry.get("isCompactSummary"):
            if isinstance(content, list) and any(c.get("type") == "tool_result" for c in content):
                for result in (c for c in content if c.get("type") == "tool_result"):
                    if "doesn't want to proceed" in text_of(result.get("content") or []):
                        print("!! TOOL REJECTED")
                continue
            text = clean(text_of(content))
            if not text or text.startswith(("Caveat:", "<task-notification>", "<command-name>/compact")): continue
            if header: print(header); header = ""
            print(f"--- [{tools} tools] ASSISTANT: {truncate(last_reply, 500)}\n>>> USER: {truncate(text, 1500)}")
            tools = 0
    print(f"--- [{tools} tools] FINAL: {truncate(last_reply, 500)}\n")
