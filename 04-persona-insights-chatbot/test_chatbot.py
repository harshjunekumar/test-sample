"""Offline tests: check the tools and the tool loop without calling the real API.
Run: python test_chatbot.py
"""
import json
from types import SimpleNamespace as NS

import chatbot
from persona_tools import PERSONA_NAMES, run_tool


def test_tools():
    out, err = run_tool("list_personas", {})
    data = json.loads(out)
    assert not err and len(data["personas"]) == len(PERSONA_NAMES)
    assert abs(sum(p["revenue_share_pct"] for p in data["personas"]) - 100) < 0.5
    out, err = run_tool("compare_personas", {"persona_a": "tech", "persona_b": "deal"})
    assert not err and "comparison" in json.loads(out)
    out, err = run_tool("persona_breakdown", {"persona_name": "beauty", "dimension": "region"})
    assert not err and len(json.loads(out)["rows"]) == 4
    _, err = run_tool("get_persona_profile", {"persona_name": "nonexistent"})
    assert err, "unknown persona should come back as an error result"


def test_tool_loop():
    """Fake Claude: first asks for a tool, then answers. Checks the loop wiring."""
    replies = iter([
        NS(stop_reason="tool_use", content=[NS(type="tool_use", id="t1", name="list_personas", input={})]),
        NS(stop_reason="end_turn", content=[NS(type="text", text="Tech buyers drive 42% of revenue.")]),
    ])
    fake_client = NS(beta=NS(messages=NS(create=lambda **kw: next(replies))))
    messages = [{"role": "user", "content": "Who drives revenue?"}]
    chatbot.ask(fake_client, messages)
    roles = [m["role"] for m in messages]
    assert roles == ["user", "assistant", "user", "assistant"], roles
    assert messages[2]["content"][0]["tool_use_id"] == "t1"


if __name__ == "__main__":
    test_tools()
    test_tool_loop()
    print("All tests passed")
