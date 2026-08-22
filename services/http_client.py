"""NOT AI. Every construct here previously produced a false positive.

Kept in the fixture deliberately: these are the exact shapes that made
every repository look like it ran an AI agent.
"""
import urllib.request

USER_AGENT = "fixture-client/1.0"


def fetch(url: str):
    # The HTTP header: the token sits at the TAIL of a compound, so it is not
    # an AI agent. This shape produced 17 of 22 evidences on a live asset.
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req)


def build(user_agent: str = None):
    user_agent = user_agent or USER_AGENT
    return {"user_agent": user_agent, "content-type": "application/json"}


# Ordinary words that happen to CONTAIN a three-letter AI acronym in their
# middle. They matched as substrings until word boundaries were added on
# 2026-08-21. None of them has anything to do with AI, and this file must
# therefore produce no evidence at all.
storage_backend = "s3"
coverage_report: dict = {}
average_latency = 0.0
leverage_ratio = 0.0
