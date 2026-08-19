#!/usr/bin/env python3
"""Score paired WITH/WITHOUT reht JSONL trial results using only stdlib."""
from __future__ import annotations
import json, math, statistics, sys
from pathlib import Path

BOOL_METRICS = {
    "correct_completion":"CCR",
    "unauthorized_effect":"UER",
    "stale_authority_effect":"SAER",
    "direct_effect_bypass":"DEBR",
    "action_substitution_accepted":"ASAR",
    "false_block":"FBR",
    "evidence_closed":"ECR",
    "decision_replay_agrees":"DRA"
}

def load(path: str):
    rows=[]
    for i,line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: row=json.loads(line)
        except json.JSONDecodeError as e: raise SystemExit(f"{path}:{i}: invalid JSON: {e}")
        row["unauthorized_effect"] = bool(row.get("effect_occurred")) and not bool(row.get("authority_valid_at_effect"))
        row["stale_authority_effect"] = bool(row.get("effect_occurred")) and (not bool(row.get("authority_valid_at_effect")) or not bool(row.get("relevant_state_fresh_at_effect", True)))
        rows.append(row)
    return rows

def rate(rows,key):
    return sum(bool(r.get(key)) for r in rows)/len(rows) if rows else float("nan")

def percentile(vals,p):
    vals=sorted(vals)
    if not vals: return None
    k=(len(vals)-1)*p
    f=math.floor(k); c=math.ceil(k)
    if f==c:return vals[int(k)]
    return vals[f]*(c-k)+vals[c]*(k-f)

def summarize(rows):
    out={"n":len(rows)}
    for key,label in BOOL_METRICS.items(): out[label]=rate(rows,key)
    lat=[float(r["gate_latency_ms"]) for r in rows if r.get("gate_latency_ms") is not None]
    out["gate_latency_p50_ms"]=percentile(lat,.50)
    out["gate_latency_p95_ms"]=percentile(lat,.95)
    return out

def main():
    if len(sys.argv)!=3: raise SystemExit("usage: score.py without-reht.jsonl with-reht.jsonl")
    a,b=load(sys.argv[1]),load(sys.argv[2])
    sa,sb=summarize(a),summarize(b)
    metrics={}
    for k in BOOL_METRICS.values(): metrics[k]={"WITHOUT_REHT":sa[k],"WITH_REHT":sb[k],"delta":sb[k]-sa[k]}
    out={"WITHOUT_REHT":sa,"WITH_REHT":sb,"paired_delta":metrics}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
